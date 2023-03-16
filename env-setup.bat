@echo off
setlocal

REM Create a new virtual environment
python -m venv env

REM Activate the virtual environment
call env\Scripts\activate.bat

REM Install required packages
pip install -r requirements.txt

REM Deactivate the virtual environment
deactivate

echo Setup complete.
pause