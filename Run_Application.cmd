@echo off
title Universal Unit Converter Launcher
color 0B
mode con: cols=90 lines=28

cls
echo.
echo ==============================================================================
echo.
echo UNIVERSAL UNIT CONVERTER
echo.
echo ==============================================================================
echo.
echo Universal Unit Converter is a modern desktop application for
echo converting values across multiple categories including:
echo.
echo   - Length
echo   - Weight
echo   - Temperature
echo   - Volume
echo   - Speed
echo   - Data Storage
echo   - Currency Exchange
echo   - And many more...
echo.
echo Features:
echo.
echo   * Conversion History
echo   * Favorites Management
echo   * Analytics Dashboard
echo   * Currency Conversion
echo   * Customizable Settings
echo.
echo Developed by Karmendra B. Srivastava
echo.
echo ==============================================================================
echo.
echo Press ENTER to launch Universal Unit Converter...
echo.

set /p dummy=

cls
echo.
echo Initializing application...
timeout /t 1 >nul

echo Loading converter modules...
timeout /t 1 >nul

echo Opening Universal Unit Converter...
timeout /t 1 >nul

python main.py

exit
