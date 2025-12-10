# 🎨 AdSnap Studio

<div align="center">

![AdSnap Studio Banner](https://img.shields.io/badge/AI-Powered-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-green?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32.0-red?style=for-the-badge&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**An AI-Powered Image Generation & Editing Platform**

Transform your creative workflow with professional-grade AI tools for image generation, product photography, and intelligent editing.

[Demo Video](#demo) • [Features](#features) • [Installation](#installation) • [Usage](#usage)

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Demo](#demo)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Integration](#api-integration)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 🌟 Overview

AdSnap Studio is a comprehensive AI-powered platform that brings professional-grade image generation and editing capabilities to your fingertips. Built with Streamlit and powered by Bria API, it's designed for content creators, marketers, e-commerce businesses, and creative professionals who need fast, high-quality visual content.

### Why AdSnap Studio?

- 🚀 **Fast & Efficient** - Generate professional images in seconds
- 🎯 **Purpose-Built** - Designed specifically for product photography and marketing
- 💰 **Cost-Effective** - Reduce expensive photoshoot costs
- 🎨 **Creative Freedom** - Unlimited possibilities with AI-powered tools
- 👥 **User-Friendly** - Intuitive interface, no technical expertise required

---

## ✨ Features

### 1. 🎨 AI Image Generation
- Transform text prompts into stunning, high-quality images
- **Smart Prompt Enhancement** - AI-powered prompt optimization for better results
- Multiple aspect ratios (1:1, 16:9, 9:16, 4:3, 3:4)
- Various artistic styles (Realistic, Artistic, Cartoon, Watercolor, Oil Painting)
- Generate up to 4 variations simultaneously
- Content moderation for safe, appropriate outputs

### 2. 📸 Lifestyle Shot Creator
Transform plain product images into professional lifestyle photography:
- **Text-to-Scene** - Describe the environment, let AI create it
- **Reference Image Mode** - Upload a reference scene for consistent styling
- Multiple placement options:
  - Automatic intelligent placement
  - Manual position control
  - Custom coordinates for precise positioning
  - Padding-based placement
- Adjustable shot sizes and product dimensions
- Background removal integration
- Generate multiple variations (up to 8)

### 3. 🎨 Generative Fill
Seamlessly edit and enhance images:
- Interactive canvas for mask drawing
- Paint over areas to regenerate them
- Negative prompts to avoid unwanted elements
- Multiple variations support
- Seed-based reproducibility
- Perfect for adding/modifying image elements

### 4. 🧹 Smart Erase
Intelligent object removal:
- Draw over unwanted elements
- AI reconstructs the background naturally
- No visible artifacts or traces
- Perfect for cleaning up images

### 5. 🎯 Product Photography Tools
- **Packshot Creator** - Professional product shots with custom backgrounds
- **Shadow Generator** - Add natural or drop shadows with full control
- **Background Removal** - Automatic subject isolation
- Custom SKU tracking for inventory management

---

# 🎥 Demo

## ⭐ Image Generation
<img width="100%" alt="Image Generation Demo" src="https://github.com/user-attachments/assets/5fb2d52c-8140-4f60-8489-de5be31812f8" />
<p><i>Generate professional images from simple text prompts</i></p>

---

## ⭐ Lifestyle Shot
<img width="100%" alt="Lifestyle Shot Demo" src="https://github.com/user-attachments/assets/6a7278e0-4b4d-4c1c-873b-351c52cb9b78" />
<p><i>Transform product photos into lifestyle scenes</i></p>

---

## ⭐ Generative Fill
<img width="100%" alt="Generative Fill Demo" src="https://github.com/user-attachments/assets/f8117041-2c0c-4e08-9095-509257be501c" />
<p><i>Edit specific areas with AI-powered regeneration</i></p>

---

## ⭐ Erase Elements
<img width="100%" alt="Erase Elements Demo" src="https://github.com/user-attachments/assets/0e14a080-659f-4670-b80a-837e8653d7dc" />
<p><i>Remove unwanted objects intelligently</i></p>

---

## 🛠️ Tech Stack

### Core Technologies
- **Python 3.8+** - Primary programming language
- **Streamlit 1.32.0** - Web application framework
- **Bria API** - AI image generation and editing engine

### Libraries & Dependencies
```
streamlit==1.32.0           # Web framework
requests==2.31.0            # HTTP requests
python-dotenv==1.0.1        # Environment variables
Pillow==10.2.0              # Image processing
python-magic==0.4.27        # File type detection
streamlit-drawable-canvas   # Interactive drawing
numpy>=1.24.0               # Numerical operations
```

### Architecture
- **Frontend**: Streamlit for reactive UI
- **Backend**: Python service layer for API integration
- **API**: RESTful integration with Bria AI services
- **State Management**: Streamlit session state

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Bria API key ([Get one here](https://bria.ai))

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/adsnap-studio.git
cd adsnap-studio
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables
Create a `.env` file in the root directory:
```env
BRIA_API_KEY=your_api_key_here
```

---

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `BRIA_API_KEY` | Your Bria API authentication key | Yes |

### API Key Setup

1. Visit [Bria AI Platform](https://bria.ai)
2. Create an account or sign in
3. Navigate to API Keys section
4. Generate a new API key
5. Copy the key to your `.env` file

---

## 🚀 Usage

### Running the Application

```bash
streamlit run app.py
```

The application will start at `http://localhost:8501`

### Basic Workflow

#### 1. Generate Images
```
1. Navigate to "Generate Image" tab
2. Enter your prompt (e.g., "A professional product photo of a watch")
3. (Optional) Click "Enhance Prompt" for AI optimization
4. Select number of images, aspect ratio, and style
5. Click "Generate Images"
```

#### 2. Create Lifestyle Shots
```
1. Go to "Lifestyle Shot" tab
2. Upload your product image
3. Select "Lifestyle Shot" from edit options
4. Choose between text prompt or reference image
5. Configure placement and generation settings
6. Enter scene description or upload reference
7. Click "Generate Lifestyle Shot"
```

#### 3. Use Generative Fill
```
1. Open "Generative Fill" tab
2. Upload your image
3. Draw a mask over the area to modify
4. Describe what you want in that area
5. (Optional) Add negative prompt
6. Click "Generate"
```

#### 4. Erase Elements
```
1. Navigate to "Erase Elements" tab
2. Upload your image
3. Draw over objects to remove
4. Click "Erase Selected Area"
```

---

## 🔌 API Integration

### Service Architecture

```
services/
├── __init__.py                    # Service exports
├── background_service.py          # Background removal
├── erase_foreground.py           # Object erasing
├── generative_fill.py            # Inpainting
├── hd_image_generation.py        # Image generation
├── lifestyle_shot.py             # Lifestyle photography
├── packshot.py                   # Product packshots
├── prompt_enhancement.py         # Prompt optimization
└── shadow.py                     # Shadow effects
```

### Example API Usage

```python
from services import generate_hd_image

# Generate an image
result = generate_hd_image(
    prompt="A professional product photo",
    api_key="your_api_key",
    num_results=1,
    aspect_ratio="1:1",
    sync=True,
    enhance_image=True
)

# Access result
image_url = result["result_url"]
```

---

## 📁 Project Structure

```
adsnap-studio/
│
├── app.py                        # Main Streamlit application
├── requirements.txt              # Python dependencies
├── .env                          # Environment variables (not in repo)
├── .env.example                  # Environment template
├── README.md                     # This file
│
├── services/                     # API service layer
│   ├── __init__.py
│   ├── background_service.py
│   ├── erase_foreground.py
│   ├── generative_fill.py
│   ├── hd_image_generation.py
│   ├── lifestyle_shot.py
│   ├── packshot.py
│   ├── prompt_enhancement.py
│   └── shadow.py
│
├── components/                   # Reusable UI components
│   ├── image_preview.py
│   ├── sidebar.py
│   └── uploader.py
│
├── utils/                        # Utility functions
│   └── helpers.py
│
├── screenshots/                  # Demo images for README
│
└── docs/                         # Additional documentation
    ├── API.md
    └── CONTRIBUTING.md
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Reporting Bugs
- Use GitHub Issues
- Include detailed description
- Add screenshots if applicable
- Specify your environment (OS, Python version)

### Suggesting Features
- Open a GitHub Issue with the "enhancement" label
- Describe the feature and its use case
- Explain why it would be valuable

### Pull Requests
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Setup
```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest

# Check code style
flake8 app.py services/
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

## 📞 Contact

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com
- Portfolio: [yourwebsite.com](https://yourwebsite.com)

**Project Link**: [https://github.com/yourusername/adsnap-studio](https://github.com/yourusername/adsnap-studio)

---

## 🙏 Acknowledgments

- [Bria AI](https://bria.ai) for providing the AI API
- [Streamlit](https://streamlit.io) for the amazing web framework
- [Pillow](https://python-pillow.org) for image processing capabilities
- All contributors who help improve this project

---

## 📊 Project Stats

![GitHub stars](https://img.shields.io/github/stars/yourusername/adsnap-studio?style=social)
![GitHub forks](https://img.shields.io/github/forks/yourusername/adsnap-studio?style=social)
![GitHub issues](https://img.shields.io/github/issues/yourusername/adsnap-studio)
![GitHub pull requests](https://img.shields.io/github/issues-pr/yourusername/adsnap-studio)

---

<div align="center">

**⭐ Star this repo if you find it useful!**

Made with ❤️ by [Your Name]

</div>
