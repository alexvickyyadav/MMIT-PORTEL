# Mahamaya Polytechnic Of Information Technology Shravasti
## Django + Python Full Project (PyCharm Guide)

नमस्ते! यह महामाया पॉलीटेक्निक ऑफ इन्फॉर्मेशन टेक्नोलॉजी, श्रावस्ती की पूरी वेबसाइट का तैयार Django प्रोजेक्ट है।

### PyCharm में चलाने का आसान तरीका (Only 2 Steps):

1. **PyCharm में खोलें**:
   - PyCharm ओपन करें -> **File** -> **Open** पर क्लिक करें।
   - इस अनज़िप किए गए `mpit_shravasti_django` फोल्डर को सेलेक्ट करें।

2. **PyCharm के Terminal में यह 3 कमांड चलाएं**:
   ```bash
   # 1. Virtual Environment बनाएं और ऑन करें:
   python -m venv venv
   venv\Scripts\activate       # (Windows)
   # source venv/bin/activate    # (Mac/Linux)

   # 2. Django इंस्टॉल करें:
   pip install -r requirements.txt

   # 3. सर्वर चलाएं:
   python manage.py runserver
   ```

3. **ब्राउज़र में खोलें**:
   - **वेबसाइट (Homepage)**: http://127.0.0.1:8000/
   - **एडमिन पैनल (Admin Panel)**: http://127.0.0.1:8000/admin/
     - Username: `admin`
     - Password: `admin123`
   - **स्टूडेंट लॉगिन (Student Portal)**: http://127.0.0.1:8000/student/login/
     - Enrollment: `E25271835500047`
     - Password: `student123`
   - **टीचर अटेंडेंस पोर्टल (Teacher Portal)**: http://127.0.0.1:8000/teacher/login/
     - User ID: `TCH-CSE-01`
     - Password: `teacher123`
