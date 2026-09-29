@echo off
title MMIT Shravasti - Local Server
echo ====================================================
echo Starting MMIT Shravasti Django Academic Portal...
echo ====================================================
echo.
echo [1/2] Verifying Admin, Teacher and Student logins...
python reset_admin.py
echo.
echo [2/2] Launching Django Web Server on http://127.0.0.1:8000/ ...
echo.
echo Open in your browser:
echo - Website:       http://127.0.0.1:8000/
echo - Admin Panel:   http://127.0.0.1:8000/admin/
echo - Student Portal: http://127.0.0.1:8000/student/login/
echo - Teacher Portal: http://127.0.0.1:8000/teacher/login/
echo.
echo Press Ctrl+C in this window to stop the server anytime.
echo ====================================================
echo.
python manage.py runserver
pause
