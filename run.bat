@echo off
echo Starting Smart Pest Recommender System...
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    echo Virtual environment created successfully!
    echo.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate

REM Install requirements if needed
echo Installing/updating requirements...
pip install -r requirements.txt

REM Set default API key if not set
if "%OPENWEATHER_API_KEY%"=="" (
    echo.
    echo WARNING: OPENWEATHER_API_KEY environment variable not set!
    echo Please set your OpenWeatherMap API key:
    echo set OPENWEATHER_API_KEY=your_api_key_here
    echo.
    echo You can get a free API key at: https://openweathermap.org/api
    echo.
    pause
)

REM Start the application
echo Starting the web application...
echo.
echo The application will be available at: http://localhost:5000
echo Press Ctrl+C to stop the application
echo.
python app/app.py

pause
