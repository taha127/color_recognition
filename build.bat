@echo off
setlocal

echo ========================================
echo Activating virtual environment...
echo ========================================

call .venv\Scripts\activate

if errorlevel 1 (
    echo Failed to activate virtual environment.
    pause
    exit /b 1
)

echo.
echo ========================================
echo Cleaning old build...
echo ========================================

if exist build (
    echo Removing build...
    rmdir /s /q build
)

if exist dist (
    echo Removing dist...
    rmdir /s /q dist
)

echo.
echo ========================================
echo Generating License Hash...
echo ========================================

python generate_license.py

if errorlevel 1 (
    echo.
    echo Failed to generate license hash.
    pause
    exit /b 1
)

echo.
echo ========================================
echo Building...
echo ========================================

set PYINSTALLER_ARGS=--clean --noconfirm

if not "%~1"=="" (
    echo Using UPX: %~1
    set PYINSTALLER_ARGS=%PYINSTALLER_ARGS% --upx-dir "%~1"
)

pyinstaller ColorRecognitionApp.spec %PYINSTALLER_ARGS%

if errorlevel 1 (

    echo.
    echo ========================================
    echo Build FAILED!
    echo ========================================

    if exist generated\generated_license.py (del generated\generated_license.py)

    pause
    exit /b 1
)

echo.
echo ========================================
echo Cleaning temporary files...
echo ========================================

if exist generated\generated_license.py (del generated\generated_license.py)

if exist generated\__pycache__ (rmdir /s /q generated\__pycache__)

echo.
echo ========================================
echo Build completed successfully.
echo ========================================

pause

endlocal