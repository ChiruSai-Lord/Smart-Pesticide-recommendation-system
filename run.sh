#!/bin/bash

echo "Starting Smart Pest Recommender System..."
echo

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "Virtual environment created successfully!"
    echo
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install requirements if needed
echo "Installing/updating requirements..."
pip install -r requirements.txt

# Set default API key if not set
if [ -z "$OPENWEATHER_API_KEY" ]; then
    echo
    echo "WARNING: OPENWEATHER_API_KEY environment variable not set!"
    echo "Please set your OpenWeatherMap API key:"
    echo "export OPENWEATHER_API_KEY=your_api_key_here"
    echo
    echo "You can get a free API key at: https://openweathermap.org/api"
    echo
    read -p "Press Enter to continue anyway..."
fi

# Start the application
echo "Starting the web application..."
echo
echo "The application will be available at: http://localhost:5000"
echo "Press Ctrl+C to stop the application"
echo
python app/app.py
