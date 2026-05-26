@echo off

pip install -r requirements.txt

pyinstaller build/comparador.spec --clean

pause
