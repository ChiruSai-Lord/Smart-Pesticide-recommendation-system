# Configuration file for Smart Pest Recommender System

import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent

# Flask Configuration
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-change-in-production')
    UPLOAD_FOLDER = BASE_DIR / 'uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    
    # Ensure upload folder exists
    UPLOAD_FOLDER.mkdir(exist_ok=True)

# Weather API Configuration
WEATHER_CONFIG = {
    'API_KEY': os.getenv('OPENWEATHER_API_KEY', 'your-api-key-here'),
    'BASE_URL': 'http://api.openweathermap.org/data/2.5/weather',
    'UNITS': 'metric',  # Use Celsius
    'TIMEOUT': 10
}

# Model Configuration
MODEL_CONFIG = {
    'MODEL_NAME': 'efficientnet_b0',
    'IMAGE_SIZE': (224, 224),
    'DEVICE': 'auto',  # 'auto', 'cuda', or 'cpu'
    'TOP_K': 3,  # Number of top predictions to return
    'NORMALIZATION_MEAN': [0.485, 0.456, 0.406],
    'NORMALIZATION_STD': [0.229, 0.224, 0.225]
}

# Supported File Types
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Crop Types (from knowledge base)
SUPPORTED_CROPS = [
    'tomato',
    'potato', 
    'rice',
    'wheat',
    'maize'
]

# Disease Classes (update based on your trained model)
DISEASE_CLASSES = [
    "early_blight",
    "late_blight", 
    "bacterial_spot",
    "healthy",
    "bacterial_leaf_blight",
    "rust",
    "stalk_rot"
]

# Weather Risk Thresholds
WEATHER_RISK_THRESHOLDS = {
    'HIGH_HUMIDITY': 80,  # % humidity above which risk is high
    'MEDIUM_HUMIDITY': 60,  # % humidity above which risk is medium
    'OPTIMAL_TEMP_MIN': 15,  # °C minimum for disease development
    'OPTIMAL_TEMP_MAX': 30,  # °C maximum for disease development
    'RAIN_RISK': 0.1,  # mm of rain above which risk increases
}

# Severity Thresholds
SEVERITY_THRESHOLDS = {
    'LOW': 10,      # % below which only cultural controls recommended
    'MEDIUM': 15,   # % above which biological controls added
    'HIGH': 25      # % above which chemical controls considered
}

# Application Settings
APP_CONFIG = {
    'NAME': 'Smart Pest Recommender',
    'VERSION': '1.0.0',
    'DEBUG': os.getenv('FLASK_DEBUG', 'False').lower() == 'true',
    'HOST': os.getenv('FLASK_HOST', '0.0.0.0'),
    'PORT': int(os.getenv('FLASK_PORT', 5000))
}

# Logging Configuration
LOGGING_CONFIG = {
    'LEVEL': os.getenv('LOG_LEVEL', 'INFO'),
    'FORMAT': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'FILE': BASE_DIR / 'logs' / 'app.log'
}

# Ensure logs directory exists
(LOGGING_CONFIG['FILE'].parent).mkdir(exist_ok=True)
