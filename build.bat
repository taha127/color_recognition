@echo off

echo ========================================
echo Activating virtual environment...
echo ========================================

call .venv\Scripts\activate

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
    pause
    exit /b 1
)

echo.
echo ========================================
echo Build completed successfully.
echo ========================================

pause