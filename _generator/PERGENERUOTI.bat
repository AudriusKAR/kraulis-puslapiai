@echo off
chcp 65001 >nul
cd /d "%~dp0"
set PYTHONUTF8=1
set PYTHONIOENCODING=utf-8
python build_v2_pages.py
python build_v2_pages2.py
echo.
echo Pergeneruota -> ..\site-v2\r
pause
