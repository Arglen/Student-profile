@echo off
set PYTHONPATH=C:\Users\argle\.kiro\crew\workspace\borrowhood_pkgs;C:\Users\argle\.kiro\crew\workspace
cd /d C:\Users\argle\.kiro\crew\workspace
"C:\Users\argle\AppData\Local\Programs\KiroCrew\resources\backend-dist\kirocrew-backend\python.exe" manage.py runserver 127.0.0.1:8000
pause
