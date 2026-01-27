@echo off
echo 🧠 FocusMate AI - Quick Setup Script
echo ====================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.8+ first.
    pause
    exit /b 1
)

REM Check if Node is installed
node --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Node.js is not installed. Please install Node.js 16+ first.
    pause
    exit /b 1
)

echo ✅ Prerequisites check passed!
echo.

REM Backend setup
echo 📦 Setting up Backend...
cd backend

REM Create virtual environment
python -m venv venv
echo ✅ Virtual environment created

REM Activate and install dependencies
call venv\Scripts\activate.bat
pip install -r requirements.txt
echo ✅ Backend dependencies installed
cd ..

REM Frontend setup
echo.
echo 📦 Setting up Frontend...
cd frontend
call npm install
echo ✅ Frontend dependencies installed
cd ..

echo.
echo ✅ Setup Complete!
echo.
echo 🚀 To start the application:
echo.
echo Terminal 1 (Backend):
echo   cd backend
echo   venv\Scripts\activate
echo   python app.py
echo.
echo Terminal 2 (Frontend):
echo   cd frontend
echo   npm run dev
echo.
echo Then open http://localhost:3000 in your browser
echo.
pause
