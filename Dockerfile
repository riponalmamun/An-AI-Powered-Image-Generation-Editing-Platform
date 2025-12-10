# ========== Base Image ==========
FROM python:3.10-slim

# ========== Set Work Directory ==========
WORKDIR /app

# ========== Copy Requirements ==========
COPY requirements.txt .

# ========== Install Dependencies ==========
RUN pip install --no-cache-dir -r requirements.txt

# ========== Copy Whole Project ==========
COPY . .

# ========== Expose Port ==========
EXPOSE 8000

# ========== Start Streamlit App ==========
CMD ["streamlit", "run", "app.py", "--server.port=8000", "--server.address=0.0.0.0"]
