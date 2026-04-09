@echo off
echo ====================================
echo PC Py Compiler Ultra Pro v2.0
echo Build Script
echo ====================================
echo.
echo Installing dependencies...
call npm install
echo.
echo Building Windows installer...
echo This may take several minutes...
echo.
call npm run build:win
echo.
echo ====================================
echo Build Complete!
echo ====================================
echo.
echo Find your installer in the 'dist' folder:
echo   - .exe installer
echo   - Portable version
echo.
echo Happy distributing!
pause
