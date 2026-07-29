@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo ==============================================
echo   Kraulis puslapiai - atnaujinimas internete
echo ==============================================
echo.
echo Ikeliami pakeitimai i GitHub...
git add -A
git commit -m "Atnaujinta"
git push
echo.
echo Baigta. Per mazdaug 1 minute atsinaujins:
echo   https://audriuskar.github.io/kraulis-puslapiai/
echo.
pause
