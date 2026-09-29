from django.db import models
from django.contrib.auth.models import User

class WebsiteConfig(models.Model):
    college_name = models.CharField(max_length=255, default="Mahamaya Polytechnic Of Information Technology, Shravasti")
    college_short_name = models.CharField(max_length=100, default="MMIT Shravasti")
    college_sub_title = models.CharField(max_length=255, default="Government Polytechnic Institute, Established 2016")
    established_year = models.IntegerField(default=2016)
    vikram_samvat = models.IntegerField(default=2066)
    bteup_code = models.CharField(max_length=50, default="4922")
    aicte_status = models.CharField(max_length=150, default="Approved by AICTE New Delhi & Affiliated to BTEUP Lucknow")
    email = models.EmailField(default="principal.mpitshravasti@gmail.com")
    phone = models.CharField(max_length=50, default="+91-5252-297800")
    helpline = models.CharField(max_length=50, default="+91-5252-297800")
    anti_ragging_helpline = models.CharField(max_length=50, default="1800-180-5522")
    address = models.TextField(default="Sirsiya Road, Bhinga, District Shravasti, Uttar Pradesh - 271831")

    # Hero Section
    hero_badge = models.CharField(max_length=200, default="GOVERNMENT POLYTECHNIC INSTITUTE · SIRSIYA ROAD, BHINGA")
    hero_title = models.CharField(max_length=255, default="Fostering Technical Excellence & Rural Innovation")
    hero_subtitle = models.TextField(default="Empowering Rural & Semi-Urban Youth with Industry-Aligned 3-Year Diploma Engineering in Computer Science, Electrical Engineering & Food Technology")
    banner_image = models.ImageField(upload_to='banners/', blank=True, null=True)

    # Principal Section
    principal_name = models.CharField(max_length=150, default="Dr. R. K. Srivastava")
    principal_designation = models.CharField(max_length=100, default="Principal / Head of Institution")
    principal_qualification = models.CharField(max_length=150, default="Ph.D. (Tech. Edu.), M.Tech (CSE), FIE")
    principal_photo = models.ImageField(upload_to='principal/', blank=True, null=True)
    principal_message = models.TextField(default="Welcome to Mahamaya Polytechnic of Information Technology (MPIT), Shravasti. Our dedicated mission is to impart hands-on technical skills, industry-grade practical engineering, and ethical values to rural and urban youth, preparing them to excel in competitive industries and nation-building.")

    # Institutional Profile
    about_text = models.TextField(default="Established in 2016 (Vikram Samvat 2066) by the Government of Uttar Pradesh, Mahamaya Polytechnic of Information Technology (MPIT) Shravasti is a premier state government technical diploma institution. It is affiliated with the Board of Technical Education Uttar Pradesh (BTEUP Institute Code: 4922) and approved by AICTE New Delhi.")
    vision = models.TextField(default="To emerge as a premier technical education institute in Uttar Pradesh, equipping youth with cutting-edge engineering skills, digital literacy, innovation, and professional ethics.")
    mission = models.TextField(default="To deliver quality diploma education in CSE, Electrical Engineering, and Food Technology through state-of-the-art laboratories, industrial exposure, skill development workshops, and dedicated faculty guidance.")

    class Meta:
        verbose_name = "Website Master Configuration"
        verbose_name_plural = "Website Master Configuration"

    def __str__(self):
        return f"{self.college_name} (Code: {self.bteup_code})"

class MarqueeNotice(models.Model):
    text = models.CharField(max_length=255, help_text="News ticker headline text")
    link = models.CharField(max_length=255, blank=True, default="#", help_text="Optional link URL")
    is_urgent = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=1)

    class Meta:
        ordering = ['order', '-id']
        verbose_name = "News Ticker / Announcement"
        verbose_name_plural = "News Tickers / Announcements"

    def __str__(self):
        return self.text

class Department(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=150)
    established_year = models.IntegerField(default=2016)
    intake_seats = models.IntegerField(default=60)
    hod_name = models.CharField(max_length=150)
    hod_email = models.EmailField()
    hod_phone = models.CharField(max_length=50)
    overview = models.TextField()
    laboratories = models.TextField(help_text="Comma-separated lab names")
    core_subjects = models.TextField(help_text="Comma-separated core subjects")
    image = models.ImageField(upload_to='departments/', blank=True, null=True)

    class Meta:
        verbose_name = "Academic Department"
        verbose_name_plural = "Academic Departments"

    def __str__(self):
        return f"{self.code} - {self.name}"

class FacultyStaff(models.Model):
    name = models.CharField(max_length=150)
    designation = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='faculty_members')
    qualification = models.CharField(max_length=150)
    experience_years = models.IntegerField(default=5)
    email = models.EmailField()
    mobile = models.CharField(max_length=50)
    responsibility = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='faculty/', blank=True, null=True)
    order = models.IntegerField(default=1)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Faculty & Staff Member"
        verbose_name_plural = "Faculty & Staff Members"

    def __str__(self):
        return f"{self.name} ({self.designation}) - {self.department.code}"

class CampusFacility(models.Model):
    title = models.CharField(max_length=150)
    icon_name = models.CharField(max_length=50, default="bi-laptop")
    description = models.TextField()
    highlights = models.TextField(help_text="Key highlights")
    image = models.ImageField(upload_to='facilities/', blank=True, null=True)
    order = models.IntegerField(default=1)

    class Meta:
        ordering = ['order']
        verbose_name = "Campus Facility"
        verbose_name_plural = "Campus Facilities"

    def __str__(self):
        return self.title

class Notice(models.Model):
    CATEGORY_CHOICES = [
        ('Examination', 'Examination & Results'),
        ('Admission', 'Admission & Counselling'),
        ('Scholarship', 'UP Govt Scholarship'),
        ('Holiday', 'Institute Holiday'),
        ('General', 'General Notice'),
    ]
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='General')
    date = models.DateField()
    description = models.TextField()
    is_pinned = models.BooleanField(default=False)
    is_urgent = models.BooleanField(default=False)
    attachment_name = models.CharField(max_length=100, blank=True, default='Official_Circular.pdf')
    attachment_file = models.FileField(upload_to='notices/', blank=True, null=True)

    class Meta:
        ordering = ['-is_pinned', '-date', '-id']
        verbose_name = "Official Notice"
        verbose_name_plural = "Official Notices"

    def __str__(self):
        return f"[{self.category}] {self.title}"

class GalleryPhoto(models.Model):
    CATEGORY_CHOICES = [
        ('Campus', 'Campus & Academic Block'),
        ('Labs', 'Modern Laboratories'),
        ('Events', 'Workshops & Events'),
        ('Sports', 'Sports & Activities'),
    ]
    title = models.CharField(max_length=150)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Campus')
    image = models.ImageField(upload_to='gallery/')
    upload_date = models.DateField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
    order = models.IntegerField(default=1)

    class Meta:
        ordering = ['order', '-id']
        verbose_name = "Photo Gallery Item"
        verbose_name_plural = "Photo Gallery Items"

    def __str__(self):
        return f"{self.title} ({self.category})"

class ContactInquiry(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Contact Inquiry"
        verbose_name_plural = "Contact Inquiries"

    def __str__(self):
        return f"{self.name} - {self.subject}"

class VerifiedStudentRecord(models.Model):
    enrollment_number = models.CharField(max_length=50, unique=True, help_text="e.g. E25271835500047")
    student_name = models.CharField(max_length=150)
    father_name = models.CharField(max_length=150, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    semester = models.IntegerField(default=1)
    session = models.CharField(max_length=50, default="2025-2026")
    verification_code = models.CharField(max_length=50, unique=True, help_text="e.g. MPIT-CSE-0047")
    email = models.EmailField()
    mobile = models.CharField(max_length=50)
    is_registered = models.BooleanField(default=False)

    class Meta:
        ordering = ['enrollment_number']
        verbose_name = "Verified Student Record"
        verbose_name_plural = "Verified Student Records"

    def __str__(self):
        return f"{self.enrollment_number} - {self.student_name} ({self.department.code})"

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    verified_record = models.OneToOneField(VerifiedStudentRecord, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='students/', blank=True, null=True)

    def __str__(self):
        return f"{self.verified_record.student_name} ({self.verified_record.enrollment_number})"

class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    teacher_id = models.CharField(max_length=50, unique=True, help_text="e.g. TCH-CSE-01")
    full_name = models.CharField(max_length=150)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    designation = models.CharField(max_length=100)
    mobile = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='teachers/', blank=True, null=True)

    class Meta:
        verbose_name = "Teacher Profile"
        verbose_name_plural = "Teacher Profiles"

    def __str__(self):
        return f"{self.full_name} [{self.teacher_id}]"

class AttendanceSession(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    semester = models.IntegerField()
    subject_name = models.CharField(max_length=150)
    date = models.DateField()
    taken_by = models.ForeignKey(TeacherProfile, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', '-id']
        verbose_name = "Attendance Session"
        verbose_name_plural = "Attendance Sessions"

    def __str__(self):
        return f"{self.department.code} Sem-{self.semester} | {self.subject_name} | {self.date}"

class StudentAttendanceItem(models.Model):
    session = models.ForeignKey(AttendanceSession, on_delete=models.CASCADE, related_name='items')
    student = models.ForeignKey(VerifiedStudentRecord, on_delete=models.CASCADE)
    is_present = models.BooleanField(default=False)

    class Meta:
        unique_together = ('session', 'student')
        verbose_name = "Student Attendance Item"
        verbose_name_plural = "Student Attendance Items"
