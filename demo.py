#!/usr/bin/env python3
"""
Demo script for Smart Pest Recommender System
This script demonstrates the core functionality without the web interface
"""

import os
import sys
from pathlib import Path

# Add the app directory to the Python path
sys.path.append(str(Path(__file__).parent / 'app'))

from model.classifier import DiseaseClassifier
from recommender import recommend_actions
from utils import get_weather_data

def demo_classifier():
    """Demo the disease classifier"""
    print("🔬 Testing Disease Classifier...")
    
    try:
        # Initialize classifier
        classifier = DiseaseClassifier()
        print("✅ Classifier initialized successfully")
        
        # Note: In a real scenario, you would load an actual image
        print("ℹ️  Classifier is ready to process images")
        print("   - Supported image size: 224x224 pixels")
        print("   - Model: EfficientNet-B0")
        print("   - Device: Auto-detected")
        
    except Exception as e:
        print(f"❌ Error initializing classifier: {e}")
        return False
    
    return True

def demo_weather_api():
    """Demo the weather API integration"""
    print("\n🌦️  Testing Weather API Integration...")
    
    # Get API key from environment
    api_key = os.getenv('OPENWEATHER_API_KEY')
    if not api_key:
        print("⚠️  OPENWEATHER_API_KEY not set. Using demo mode.")
        print("   Get a free API key at: https://openweathermap.org/api")
        api_key = 'demo_key'
    
    try:
        # Test weather API
        weather_data = get_weather_data('London', api_key)
        
        if weather_data and 'current' in weather_data:
            print("✅ Weather API working successfully")
            print(f"   Location: {weather_data['location']}")
            print(f"   Temperature: {weather_data['current']['temperature']}°C")
            print(f"   Humidity: {weather_data['current']['humidity']}%")
            print(f"   Conditions: {weather_data['current']['description']}")
        else:
            print("⚠️  Weather API returned limited data (demo mode)")
            
    except Exception as e:
        print(f"❌ Error testing weather API: {e}")
        return False
    
    return True

def demo_recommendations():
    """Demo the recommendation system"""
    print("\n💡 Testing Recommendation System...")
    
    try:
        # Test with sample data
        crop = 'tomato'
        disease = 'early_blight'
        severity = 25  # 25% severity
        weather = {
            'current': {
                'humidity': 85,
                'rain': 0,
                'temperature': 22
            }
        }
        
        recommendations = recommend_actions(crop, disease, severity, weather)
        
        print("✅ Recommendation system working successfully")
        print(f"   Crop: {crop}")
        print(f"   Disease: {disease}")
        print(f"   Severity: {severity}%")
        print(f"   Weather: {weather['current']['humidity']}% humidity, {weather['current']['temperature']}°C")
        
        if recommendations['actions']:
            print("   Recommendations generated:")
            for action in recommendations['actions']:
                print(f"     - {action['type'].title()}: {len(action['items'])} items")
        else:
            print("   No recommendations generated")
            
    except Exception as e:
        print(f"❌ Error testing recommendation system: {e}")
        return False
    
    return True

def demo_knowledge_base():
    """Demo the knowledge base"""
    print("\n📚 Testing Knowledge Base...")
    
    try:
        from recommender import KB
        
        print("✅ Knowledge base loaded successfully")
        print(f"   Supported crops: {', '.join(KB.keys())}")
        
        # Show sample data for tomato
        if 'tomato' in KB:
            tomato_diseases = list(KB['tomato'].keys())
            print(f"   Tomato diseases: {', '.join(tomato_diseases)}")
            
            if 'early_blight' in KB['tomato']:
                early_blight = KB['tomato']['early_blight']
                print(f"   Early blight controls:")
                if 'cultural' in early_blight:
                    print(f"     - Cultural: {len(early_blight['cultural'])} methods")
                if 'biological' in early_blight:
                    print(f"     - Biological: {len(early_blight['biological'])} methods")
                if 'chemical' in early_blight:
                    print(f"     - Chemical: {len(early_blight['chemical'])} pesticides")
        
    except Exception as e:
        print(f"❌ Error testing knowledge base: {e}")
        return False
    
    return True

def main():
    """Main demo function"""
    print("🚀 Smart Pest Recommender System - Demo Mode")
    print("=" * 50)
    
    # Test all components
    tests = [
        ("Disease Classifier", demo_classifier),
        ("Weather API", demo_weather_api),
        ("Recommendation System", demo_recommendations),
        ("Knowledge Base", demo_knowledge_base)
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ Unexpected error in {test_name}: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 Demo Results Summary:")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"   {test_name}: {status}")
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All systems are working correctly!")
        print("   You can now run the web application with: python app/app.py")
    else:
        print("⚠️  Some systems need attention before running the web application")
        print("   Check the error messages above for details")

if __name__ == "__main__":
    main()
