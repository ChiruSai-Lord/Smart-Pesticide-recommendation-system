# 🚀 Quick Setup Guide - Smart Pest Recommender

## ⚡ Get Started in 5 Minutes

### 1. **Prerequisites**
- Python 3.8+ installed
- Internet connection for weather data
- Free OpenWeatherMap API key

### 2. **Get Weather API Key** (Free)
1. Go to [OpenWeatherMap](https://openweathermap.org/api)
2. Sign up for free account
3. Get your API key
4. Set environment variable:
   ```bash
   # Windows
   set OPENWEATHER_API_KEY=your_key_here
   
   # macOS/Linux
   export OPENWEATHER_API_KEY=your_key_here
   ```

### 3. **Run the System**

#### **Option A: One-Click Start (Windows)**
```bash
# Double-click or run:
run.bat
```

#### **Option B: One-Click Start (macOS/Linux)**
```bash
# Make executable and run:
chmod +x run.sh
./run.sh
```

#### **Option C: Manual Setup**
```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start application
python app/app.py
```

### 4. **Access the Web App**
Open your browser and go to: **http://localhost:5000**

## 🧪 Test the System

Run the demo script to verify everything works:
```bash
python demo.py
```

You should see: ✅ All systems are working correctly!

## 📱 How to Use

1. **Upload Image**: Drag & drop crop image
2. **Select Crop**: Choose from dropdown
3. **Enter Location**: Your city for weather data
4. **Get Results**: AI analysis + recommendations

## 🔧 Troubleshooting

### **Common Issues**

| Problem | Solution |
|---------|----------|
| "Module not found" | Run `pip install -r requirements.txt` |
| Weather API errors | Check your API key is set correctly |
| Port already in use | Change port in `config.py` or kill existing process |
| Model loading fails | Ensure PyTorch is installed correctly |

### **Get Help**
- Check the full [README.md](README.md)
- Run `python demo.py` for system diagnostics
- Verify all dependencies are installed

## 🌟 What You Get

- **AI Disease Detection**: Upload crop image, get disease diagnosis
- **Smart Recommendations**: Cultural, biological, and chemical controls
- **Weather Integration**: Real-time environmental risk assessment
- **Dosage Guidelines**: Specific pesticide application rates
- **Safety Features**: Built-in best practices and reminders

## 🎯 Next Steps

1. **Train Your Model**: Use your own crop disease dataset
2. **Customize Knowledge Base**: Add local pesticides and regulations
3. **Deploy to Production**: Use proper hosting and security
4. **Mobile App**: Extend to smartphone application

---

**Need help?** Check the main [README.md](README.md) for detailed documentation!

