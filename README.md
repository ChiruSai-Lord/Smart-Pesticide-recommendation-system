# Smart Pest Recommender System

An AI-powered web application that provides intelligent pesticide recommendations using deep learning image analysis and real-time weather data integration.

## 🌟 Features

- **Deep Learning Disease Detection**: Uses EfficientNet-B0 model to identify crop diseases from images
- **Real-time Weather Integration**: Automatically fetches weather data from OpenWeatherMap API
- **Smart Recommendations**: Provides cultural, biological, and chemical control measures
- **Dosage Guidelines**: Includes specific pesticide dosages and application notes
- **Weather Risk Assessment**: Analyzes environmental conditions for disease development
- **Modern Web Interface**: Responsive, user-friendly design with drag-and-drop image upload
- **Safety Reminders**: Built-in safety guidelines and best practices

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- OpenWeatherMap API key (free at [openweathermap.org](https://openweathermap.org/api))

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd smart-pest-recommender
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # On Windows
   set OPENWEATHER_API_KEY=your_api_key_here
   
   # On macOS/Linux
   export OPENWEATHER_API_KEY=your_api_key_here
   ```

5. **Run the application**
   ```bash
   python app/app.py
   ```

6. **Open your browser**
   Navigate to `http://localhost:5000`

## 📱 How to Use

### 1. Upload Crop Image
- Drag and drop an image or click "Choose File"
- Supported formats: JPG, PNG, GIF
- Maximum file size: 16MB

### 2. Provide Information
- Select crop type (tomato, potato, rice, wheat, maize)
- Enter your location for weather data

### 3. Get AI Analysis
- Click "Get AI Recommendations"
- View disease detection results
- Review pesticide recommendations
- Check weather risk factors

### 4. Review Results
- Disease identification with confidence levels
- Cultural, biological, and chemical control measures
- Specific pesticide dosages and application notes
- Weather-based risk assessment
- Safety guidelines and reminders

## 🏗️ Architecture

```
smart-pest-recommender/
├── app/
│   ├── app.py              # Flask web application
│   ├── model/
│   │   ├── classifier.py   # Disease classification model
│   │   └── segmentation.py # Image segmentation (future)
│   ├── recommender.py      # Recommendation engine
│   ├── utils.py            # Utility functions & weather API
│   ├── kb.json             # Knowledge base (crops & pesticides)
│   └── templates/          # HTML templates
│       ├── index.html      # Main upload page
│       └── result.html     # Results display page
├── train/                  # Training scripts
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🔧 Configuration

### Weather API Setup
1. Sign up at [OpenWeatherMap](https://openweathermap.org/api)
2. Get your free API key
3. Set environment variable: `OPENWEATHER_API_KEY=your_key`

### Model Configuration
- **Model**: EfficientNet-B0 (configurable in `classifier.py`)
- **Image Size**: 224x224 pixels
- **Classes**: Configurable disease categories
- **Device**: Auto-detects CUDA/CPU

### Supported Crops
- Tomato (early blight, late blight, bacterial spot)
- Potato (late blight)
- Rice (bacterial leaf blight)
- Wheat (rust)
- Maize (stalk rot)

## 🧠 AI Model Details

### Disease Classifier
- **Architecture**: EfficientNet-B0
- **Input**: RGB images (224x224)
- **Output**: Disease classification with confidence scores
- **Training**: Transfer learning with custom dataset

### Recommendation Engine
- **Rule-based system** with weather integration
- **Cultural controls**: Non-chemical management practices
- **Biological controls**: Biopesticides and natural solutions
- **Chemical controls**: Synthetic pesticides with dosage guidelines

## 🌦️ Weather Integration

The system automatically fetches:
- Temperature (°C)
- Humidity (%)
- Precipitation (mm)
- Wind speed (m/s)
- Weather description

Weather data influences:
- Disease risk assessment
- Pesticide urgency
- Application timing recommendations

## 📊 API Endpoints

- `GET /` - Main application page
- `POST /upload` - Image upload and analysis
- `GET /api/weather/<location>` - Weather data for location
- `GET /api/crops` - Available crop types

## 🛡️ Safety Features

- **PPE Recommendations**: Personal protective equipment guidelines
- **Dosage Validation**: Specific application rates
- **Pre-harvest Intervals**: Safe application timing
- **Environmental Considerations**: Weather-based application advice
- **Safety Reminders**: Built-in best practices

## 🔮 Future Enhancements

- [ ] Image segmentation for precise disease localization
- [ ] Mobile app development
- [ ] Multi-language support
- [ ] Historical analysis tracking
- [ ] Integration with agricultural databases
- [ ] Real-time field monitoring
- [ ] Predictive disease modeling

## 🐛 Troubleshooting

### Common Issues

1. **Weather API Errors**
   - Check API key validity
   - Verify internet connection
   - Check location spelling

2. **Model Loading Issues**
   - Ensure PyTorch is installed correctly
   - Check model file paths
   - Verify CUDA compatibility

3. **Image Upload Problems**
   - Check file format (JPG, PNG, GIF)
   - Verify file size (< 16MB)
   - Ensure image is not corrupted

### Debug Mode
Run with debug enabled:
```bash
python app/app.py
```

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📞 Support

For support and questions:
- Create an issue in the repository
- Contact the development team
- Check the documentation

## 🙏 Acknowledgments

- OpenWeatherMap for weather data
- PyTorch and timm for deep learning models
- Bootstrap for UI components
- Font Awesome for icons

---

**Note**: This system provides recommendations based on AI analysis and should be used alongside professional agricultural advice. Always follow local regulations and pesticide labels.

