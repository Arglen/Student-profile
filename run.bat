@echo off
set PYTHONPATH=C:\Users\argle\.kiro\crew\workspace\borrowhood_pkgs;C:\Users\argle\workplace\student-profile
cd /d C:\Users\argle\workplace\student-profile
"C:\Users\argle\AppData\Local\Programs\KiroCrew\resources\backend-dist\kirocrew-backend\python.exe" manage.py runserver 127.0.0.1:8000
pause
