@echo off
setlocal enabledelayedexpansion

set "firstLineSkipped=false"

for /f "tokens=1,2 delims=," %%a in (sample_data.csv) do (
    if "!firstLineSkipped!"=="true" (
        echo Sending row: %%a, %%b
        curl -s -X POST http://127.0.0.1:5000/submit -d "name=%%a" -d "location=%%b" >nul
        echo Waiting 5 seconds before next row...
        timeout /t 5 /nobreak >nul
    ) else (
        set "firstLineSkipped=true"
    )
)

echo.
echo All rows sent successfully!
echo Opening submitted data in browser...

:: Open the /view page in the default browser
start http://127.0.0.1:5000/view
