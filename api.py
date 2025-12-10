from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from services import (
    lifestyle_shot_by_text,
    lifestyle_shot_by_image,
    enhance_prompt,
    generate_hd_image,
    erase_foreground,
    generative_fill,
    add_shadow,
    create_packshot
)
import os
from dotenv import load_dotenv
from typing import Optional
import tempfile

load_dotenv()

app = FastAPI(
    title="AdSnap Studio API",
    description="AI-Powered Image Generation & Editing Platform - Transform your visual content with AI",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get API key from environment
BRIA_API_KEY = os.getenv("BRIA_API_KEY")

@app.get("/")
def read_root():
    """Welcome endpoint with API information"""
    return {
        "message": "Welcome to AdSnap Studio API",
        "version": "1.0.0",
        "documentation": "/docs",
        "redoc": "/redoc",
        "endpoints": {
            "generate_image": "/api/generate-image",
            "enhance_prompt": "/api/enhance-prompt",
            "lifestyle_shot_text": "/api/lifestyle-shot/text",
            "lifestyle_shot_image": "/api/lifestyle-shot/image",
            "generative_fill": "/api/generative-fill",
            "erase_foreground": "/api/erase-foreground",
            "add_shadow": "/api/add-shadow",
            "create_packshot": "/api/create-packshot"
        }
    }

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "api_key_configured": bool(BRIA_API_KEY)
    }

@app.post("/api/generate-image")
async def generate_image(
    prompt: str = Form(..., description="Text description of the image to generate"),
    num_results: int = Form(1, ge=1, le=4, description="Number of images to generate (1-4)"),
    aspect_ratio: str = Form("1:1", description="Aspect ratio (1:1, 16:9, 9:16, 4:3, 3:4)"),
    enhance_image: bool = Form(True, description="Enhance image quality"),
    medium: str = Form("photography", description="Medium type (photography, art)"),
    api_key: Optional[str] = Form(None, description="API key (optional if set in environment)")
):
    """
    Generate professional images from text prompts
    
    **Parameters:**
    - **prompt**: Detailed description of what you want to generate
    - **num_results**: How many variations to create (1-4)
    - **aspect_ratio**: Image dimensions ratio
    - **enhance_image**: Apply quality enhancement
    - **medium**: Art style - photography or art
    """
    try:
        key = api_key or BRIA_API_KEY
        if not key:
            raise HTTPException(status_code=401, detail="API key is required")
        
        result = generate_hd_image(
            prompt=prompt,
            api_key=key,
            num_results=num_results,
            aspect_ratio=aspect_ratio,
            sync=True,
            enhance_image=enhance_image,
            medium=medium,
            prompt_enhancement=False,
            content_moderation=True
        )
        
        return JSONResponse(content={
            "status": "success",
            "data": result,
            "message": "Image generated successfully"
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/enhance-prompt")
async def enhance_text_prompt(
    prompt: str = Form(..., description="Original text prompt to enhance"),
    api_key: Optional[str] = Form(None, description="API key (optional if set in environment)")
):
    """
    Enhance a text prompt for better image generation results
    
    **Parameters:**
    - **prompt**: Your original prompt
    
    **Returns:**
    - Enhanced, detailed version of your prompt
    """
    try:
        key = api_key or BRIA_API_KEY
        if not key:
            raise HTTPException(status_code=401, detail="API key is required")
        
        enhanced = enhance_prompt(key, prompt)
        
        return JSONResponse(content={
            "status": "success",
            "original": prompt,
            "enhanced": enhanced,
            "message": "Prompt enhanced successfully"
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/lifestyle-shot/text")
async def lifestyle_shot_text(
    file: UploadFile = File(..., description="Product image file"),
    scene_description: str = Form(..., description="Describe the environment/scene"),
    placement_type: str = Form("automatic", description="Placement type (original, automatic, manual_placement)"),
    num_results: int = Form(4, ge=1, le=8, description="Number of results (1-8)"),
    sync: bool = Form(False, description="Wait for results vs get URLs immediately"),
    fast: bool = Form(True, description="Fast mode - balance speed and quality"),
    api_key: Optional[str] = Form(None, description="API key (optional if set in environment)")
):
    """
    Create lifestyle product photography using text description
    
    **Parameters:**
    - **file**: Your product image
    - **scene_description**: Describe where you want the product placed
    - **placement_type**: How to position the product
    - **num_results**: Number of variations
    - **sync**: Wait for completion or get URLs
    - **fast**: Enable fast generation mode
    """
    try:
        key = api_key or BRIA_API_KEY
        if not key:
            raise HTTPException(status_code=401, detail="API key is required")
        
        # Read file content
        image_data = await file.read()
        
        result = lifestyle_shot_by_text(
            api_key=key,
            image_data=image_data,
            scene_description=scene_description,
            placement_type=placement_type,
            num_results=num_results,
            sync=sync,
            fast=fast,
            optimize_description=True,
            shot_size=[1000, 1000],
            original_quality=False,
            exclude_elements=None,
            manual_placement_selection=["upper_left"],
            padding_values=[0, 0, 0, 0],
            foreground_image_size=None,
            foreground_image_location=None,
            force_rmbg=False,
            content_moderation=True,
            sku=None
        )
        
        return JSONResponse(content={
            "status": "success",
            "data": result,
            "message": "Lifestyle shot created successfully"
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/lifestyle-shot/image")
async def lifestyle_shot_image(
    file: UploadFile = File(..., description="Product image file"),
    reference_image: UploadFile = File(..., description="Reference environment image"),
    placement_type: str = Form("automatic", description="Placement type"),
    num_results: int = Form(4, ge=1, le=8, description="Number of results (1-8)"),
    sync: bool = Form(False, description="Synchronous mode"),
    api_key: Optional[str] = Form(None, description="API key (optional if set in environment)")
):
    """
    Create lifestyle shot using a reference image
    
    **Parameters:**
    - **file**: Your product image
    - **reference_image**: Example environment/scene image
    - **placement_type**: How to position the product
    - **num_results**: Number of variations
    - **sync**: Wait for completion
    """
    try:
        key = api_key or BRIA_API_KEY
        if not key:
            raise HTTPException(status_code=401, detail="API key is required")
        
        # Read file contents
        image_data = await file.read()
        ref_data = await reference_image.read()
        
        result = lifestyle_shot_by_image(
            api_key=key,
            image_data=image_data,
            reference_image=ref_data,
            placement_type=placement_type,
            num_results=num_results,
            sync=sync,
            shot_size=[1000, 1000],
            original_quality=False,
            manual_placement_selection=["upper_left"],
            padding_values=[0, 0, 0, 0],
            foreground_image_size=None,
            foreground_image_location=None,
            force_rmbg=False,
            content_moderation=True,
            sku=None,
            enhance_ref_image=True,
            ref_image_influence=1.0
        )
        
        return JSONResponse(content={
            "status": "success",
            "data": result,
            "message": "Lifestyle shot created successfully"
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/generative-fill")
async def generative_fill_endpoint(
    image: UploadFile = File(..., description="Original image"),
    mask: UploadFile = File(..., description="Mask image (white=fill, black=keep)"),
    prompt: str = Form(..., description="What to generate in masked area"),
    negative_prompt: Optional[str] = Form(None, description="What to avoid"),
    num_results: int = Form(1, ge=1, le=4, description="Number of variations"),
    sync: bool = Form(False, description="Synchronous mode"),
    api_key: Optional[str] = Form(None, description="API key (optional if set in environment)")
):
    """
    Fill selected areas of an image with AI-generated content
    
    **Parameters:**
    - **image**: Your base image
    - **mask**: White areas will be filled, black areas preserved
    - **prompt**: Describe what to generate
    - **negative_prompt**: What to avoid in generation
    - **num_results**: Number of variations
    - **sync**: Wait for completion
    """
    try:
        key = api_key or BRIA_API_KEY
        if not key:
            raise HTTPException(status_code=401, detail="API key is required")
        
        # Read files
        image_data = await image.read()
        mask_data = await mask.read()
        
        result = generative_fill(
            key,
            image_data,
            mask_data,
            prompt,
            negative_prompt=negative_prompt,
            num_results=num_results,
            sync=sync,
            seed=None,
            content_moderation=True
        )
        
        return JSONResponse(content={
            "status": "success",
            "data": result,
            "message": "Generative fill completed successfully"
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/erase-foreground")
async def erase_foreground_endpoint(
    image: UploadFile = File(..., description="Image with elements to erase"),
    content_moderation: bool = Form(False, description="Enable content moderation"),
    api_key: Optional[str] = Form(None, description="API key (optional if set in environment)")
):
    """
    Intelligently erase elements from images
    
    **Parameters:**
    - **image**: Image containing elements to remove
    - **content_moderation**: Check content safety
    """
    try:
        key = api_key or BRIA_API_KEY
        if not key:
            raise HTTPException(status_code=401, detail="API key is required")
        
        image_data = await image.read()
        
        result = erase_foreground(
            key,
            image_data=image_data,
            content_moderation=content_moderation
        )
        
        return JSONResponse(content={
            "status": "success",
            "data": result,
            "message": "Elements erased successfully"
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/add-shadow")
async def add_shadow_endpoint(
    image: UploadFile = File(..., description="Product image"),
    shadow_type: str = Form("natural", description="Shadow type (natural, drop)"),
    background_color: Optional[str] = Form(None, description="Background color (hex)"),
    shadow_intensity: int = Form(60, ge=0, le=100, description="Shadow intensity (0-100)"),
    api_key: Optional[str] = Form(None, description="API key (optional if set in environment)")
):
    """
    Add professional shadows to product images
    
    **Parameters:**
    - **image**: Your product image
    - **shadow_type**: Type of shadow effect
    - **background_color**: Optional background color
    - **shadow_intensity**: Shadow strength (0-100)
    """
    try:
        key = api_key or BRIA_API_KEY
        if not key:
            raise HTTPException(status_code=401, detail="API key is required")
        
        image_data = await image.read()
        
        result = add_shadow(
            api_key=key,
            image_data=image_data,
            shadow_type=shadow_type,
            background_color=background_color,
            shadow_color="#000000",
            shadow_offset=[0, 15],
            shadow_intensity=shadow_intensity,
            shadow_blur=20,
            shadow_width=None,
            shadow_height=70,
            sku=None,
            force_rmbg=False,
            content_moderation=True
        )
        
        return JSONResponse(content={
            "status": "success",
            "data": result,
            "message": "Shadow added successfully"
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/create-packshot")
async def create_packshot_endpoint(
    image: UploadFile = File(..., description="Product image"),
    background_color: str = Form("#FFFFFF", description="Background color (hex)"),
    force_rmbg: bool = Form(False, description="Force background removal"),
    api_key: Optional[str] = Form(None, description="API key (optional if set in environment)")
):
    """
    Create professional product packshots with clean backgrounds
    
    **Parameters:**
    - **image**: Your product image
    - **background_color**: Desired background color
    - **force_rmbg**: Force background removal first
    """
    try:
        key = api_key or BRIA_API_KEY
        if not key:
            raise HTTPException(status_code=401, detail="API key is required")
        
        image_data = await image.read()
        
        result = create_packshot(
            key,
            image_data,
            background_color=background_color,
            sku=None,
            force_rmbg=force_rmbg,
            content_moderation=True
        )
        
        return JSONResponse(content={
            "status": "success",
            "data": result,
            "message": "Packshot created successfully"
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    print("Starting AdSnap Studio API Server...")
    print(f"API Key configured: {bool(BRIA_API_KEY)}")
    print("Swagger UI will be available at: http://localhost:8000/docs")
    print("ReDoc will be available at: http://localhost:8000/redoc")
    
    uvicorn.run(
        "api:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )