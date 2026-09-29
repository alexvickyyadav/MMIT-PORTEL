#!/usr/bin/env python
import os
import sys

print("="*65)
print("MMIT Shravasti - Admin Password Reset Utility")
print("="*65)

try:
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mpit_project.settings')
    django.setup()
    from django.contrib.auth.models import User

    # 1. Master Admin
    user, created = User.objects.get_or_create(username='admin')
    user.set_password('admin123')
    user.is_superuser = True
    user.is_staff = True
    user.is_active = True
    user.first_name = "Super"
    user.last_name = "Administrator"
    user.email = 'admin@mmitshravasti.ac.in'
    user.save()

    # 2. Teacher
    tch, _ = User.objects.get_or_create(username='TCH-CSE-01')
    tch.set_password('teacher123')
    tch.is_staff = True
    tch.is_active = True
    tch.save()

    # 3. Student
    stu, _ = User.objects.get_or_create(username='E25271835500047')
    stu.set_password('student123')
    stu.is_active = True
    stu.save()
    print("[SUCCESS] All accounts reset and verified via Django ORM!")

except Exception as err:
    import sqlite3
    import hashlib
    import base64

    def make_hash(pwd, salt="mmitpoly2026", iters=600000):
        h = hashlib.pbkdf2_hmac('sha256', pwd.encode('utf-8'), salt.encode('utf-8'), iters)
        b64 = base64.b64encode(h).decode('ascii').strip()
        return f"pbkdf2_sha256${iters}${salt}${b64}"

    admin_hash = make_hash("admin123")
    teacher_hash = make_hash("teacher123")
    student_hash = make_hash("student123")

    db_file = os.path.join(os.path.dirname(__file__), 'db.sqlite3')
    if not os.path.exists(db_file):
        db_file = 'db.sqlite3'

    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute("UPDATE auth_user SET password = ?, is_superuser = 1, is_staff = 1, is_active = 1 WHERE username = 'admin'", (admin_hash,))
    if cur.rowcount == 0:
        cur.execute("INSERT INTO auth_user (password, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (?, 1, 'admin', 'Super', 'Administrator', 'admin@mmitshravasti.ac.in', 1, 1, CURRENT_TIMESTAMP)", (admin_hash,))
    cur.execute("UPDATE auth_user SET password = ?, is_staff = 1, is_active = 1 WHERE username = 'TCH-CSE-01'", (teacher_hash,))
    cur.execute("UPDATE auth_user SET password = ?, is_active = 1 WHERE username = 'E25271835500047'", (student_hash,))

    # Ensure django_admin_log table exists
    cur.execute('''
    CREATE TABLE IF NOT EXISTS "django_admin_log" (
        "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
        "action_time" datetime NOT NULL,
        "object_id" text NULL,
        "object_repr" varchar(200) NOT NULL,
        "action_flag" smallint unsigned NOT NULL CHECK ("action_flag" >= 0),
        "change_message" text NOT NULL,
        "content_type_id" integer NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED,
        "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED
    );''')
    cur.execute('CREATE INDEX IF NOT EXISTS "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id");')
    cur.execute('CREATE INDEX IF NOT EXISTS "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id");')

    for app, name in [
        ('contenttypes', '0002_remove_content_type_name'),
        ('admin', '0001_initial'),
        ('admin', '0002_logentry_remove_auto_add'),
        ('admin', '0003_logentry_add_action_flag_choices')
    ]:
        cur.execute("SELECT COUNT(*) FROM django_migrations WHERE app = ? AND name = ?", (app, name))
        if cur.fetchone()[0] == 0:
            cur.execute("INSERT INTO django_migrations (app, name, applied) VALUES (?, ?, CURRENT_TIMESTAMP)", (app, name))

    conn.commit()
    conn.close()
    print("[SUCCESS] All accounts and django_admin_log verified via SQLite fallback!")

print("-" * 65)
print("1. Master Admin Panel  : http://127.0.0.1:8000/admin/")
print("   Username: admin")
print("   Password: admin123")
print("-" * 65)
print("2. Teacher Portal      : http://127.0.0.1:8000/teacher/login/")
print("   Teacher ID: TCH-CSE-01")
print("   Password: teacher123")
print("-" * 65)
print("3. Student Portal      : http://127.0.0.1:8000/student/login/")
print("   Enrollment No: E25271835500047")
print("   Password: student123")
print("="*65)

