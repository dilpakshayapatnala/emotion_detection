@echo off
:: Run this batch file as admin if possible

echo ================================
echo AI Emotion Detection - Setup
echo ================================

:: Check Python version
python --version
if %ERRORLEVEL% NEQ 0 (
    echo Python not found! Please install Python 3 and add to PATH.
    pause
    exit /b
)

:: Ensure pip is installed and upgraded
python -m ensurepip --upgrade
python -m pip install --upgrade pip

:: Install dependencies
echo Installing required packages...
python -m pip install -r requirements.txt

:: Run Flask app
echo Starting the AI Emotion Detection app...
python app.py

pause
