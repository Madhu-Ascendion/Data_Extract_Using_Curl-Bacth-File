@echo off
setlocal enabledelayedexpansion

for /f "tokens=1,2 delims=," %%a in (sample_data.csv) do (
    echo Sending row: %%a, %%b
    curl -X POST http://127.0.0.1:5000/submit -d "name=%%a" -d "location=%%b"
    timeout /t 5 >nul
)

endlocal
