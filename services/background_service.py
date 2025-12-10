import requests
import json

def remove_background(api_key, image_data, content_moderation=False):
    """
    Remove background from an image using the Bria API.
    
    Args:
        api_key: Bria API key
        image_data: Image data as bytes
        content_moderation: Enable content moderation
        
    Returns:
        dict: API response with result_url
    """
    url = "https://engine.prod.bria-api.com/v1/background/remove"
    
    headers = {
        "api_token": api_key
    }
    
    files = {
        "file": ("image.png", image_data, "image/png")
    }
    
    data = {}
    if content_moderation:
        data["content_moderation"] = "true"
    
    try:
        response = requests.post(url, headers=headers, files=files, data=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Background removal failed: {str(e)}")