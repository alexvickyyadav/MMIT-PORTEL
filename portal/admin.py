from django.contrib import admin
from django.utils.html import format_html
from .models import (
    WebsiteConfig, MarqueeNotice, Department, FacultyStaff,
    CampusFacility, Notice, GalleryPhoto, ContactInquiry,
    VerifiedStudentRecord, StudentProfile, TeacherProfile,
    AttendanceSession, StudentAttendanceItem
)

admin.site.site_header = "MMIT Shravasti - Master CMS & Academic Administration"
admin.site.site_title = "MMIT Portal Admin"
admin.site.index_title = "MMIT Shravasti Central Dashboard - Manage Website Content, Photos & Records"

@admin.register(WebsiteConfig)
class WebsiteConfigAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Basic Institutional Information", {
            "fields": ("college_name", "college_short_name", "college_sub_title", "bteup_code", "aicte_status", "established_year", "vikram_samvat")
        }),
        ("Contact & Helplines", {
            "fields": ("phone", "helpline", "anti_ragging_helpline", "email", "address")
        }),
        ("Homepage Hero Banner", {
            "fields": ("hero_badge", "hero_title", "hero_subtitle", "banner_image")
        }),
        ("Principal Desk & Photo (Editable when Principal Changes)", {
            "fields": ("principal_name", "principal_designation", "principal_qualification", "principal_photo", "principal_message")
        }),
        ("Vision, Mission & Profile", {
            "fields": ("about_text", "vision", "mission")
        }),
    )
    list_display = ('college_short_name', 'college_name', 'bteup_code', 'principal_name', 'principal_preview')

    def principal_preview(self, obj):
        if obj.principal_photo:
            return format_html('<img src="{}" width="50" height="60" style="object-fit:cover; border-radius:6px; border:2px solid #f59e0b;" />', obj.principal_photo.url)
        return "No Photo"
    principal_preview.short_description = "Principal Photo"

    def has_add_permission(self, request):
        return not WebsiteConfig.objects.exists()

@admin.register(MarqueeNotice)
class MarqueeNoticeAdmin(admin.ModelAdmin):
    list_display = ('text', 'link', 'is_urgent', 'is_active', 'order')
    list_editable = ('is_urgent', 'is_active', 'order')
    search_fields = ('text',)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'intake_seats', 'hod_name', 'hod_phone', 'image_preview')
    search_fields = ('name', 'code', 'hod_name')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" height="40" style="object-fit:cover; border-radius:4px;" />', obj.image.url)
        return "-"
    image_preview.short_description = "Department Photo"

@admin.register(FacultyStaff)
class FacultyStaffAdmin(admin.ModelAdmin):
    list_display = ('photo_preview', 'name', 'designation', 'department', 'qualification', 'experience_years', 'mobile', 'order')
    list_filter = ('department', 'designation')
    list_editable = ('order',)
    search_fields = ('name', 'qualification', 'responsibility', 'email')

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="40" height="40" style="object-fit:cover; border-radius:50%; border:1px solid #cbd5e1;" />', obj.photo.url)
        return "No Photo"
    photo_preview.short_description = "Photo"

@admin.register(CampusFacility)
class CampusFacilityAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_name', 'order', 'image_preview')
    list_editable = ('order',)
    search_fields = ('title', 'description')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" height="40" style="object-fit:cover; border-radius:4px;" />', obj.image.url)
        return "-"
    image_preview.short_description = "Facility Photo"

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date', 'is_pinned', 'is_urgent', 'attachment_name', 'pdf_link')
    list_filter = ('category', 'is_pinned', 'is_urgent', 'date')
    list_editable = ('is_pinned', 'is_urgent')
    search_fields = ('title', 'description')
    fields = ('title', 'category', 'date', 'description', 'is_pinned', 'is_urgent', 'attachment_name', 'attachment_file')

    def pdf_link(self, obj):
        if obj.attachment_file:
            return format_html('<a href="{}" target="_blank" style="background:#dc2626; color:#ffffff; padding:4px 8px; border-radius:4px; font-weight:bold; text-decoration:none; font-size:11px;">PDF File</a>', obj.attachment_file.url)
        return format_html('<span style="color:#94a3b8; font-size:11px;">No PDF</span>')
    pdf_link.short_description = "PDF Attachment"

@admin.register(GalleryPhoto)
class GalleryPhotoAdmin(admin.ModelAdmin):
    list_display = ('photo_preview', 'title', 'category', 'is_featured', 'order')
    list_filter = ('category', 'is_featured')
    list_editable = ('is_featured', 'order')
    search_fields = ('title',)

    def photo_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" height="40" style="object-fit:cover; border-radius:4px;" />', obj.image.url)
        return "-"
    photo_preview.short_description = "Preview"

@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'phone', 'email', 'created_at', 'is_resolved')
    list_filter = ('is_resolved', 'created_at')
    list_editable = ('is_resolved',)
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('name', 'email', 'phone', 'subject', 'message', 'created_at')

@admin.register(VerifiedStudentRecord)
class VerifiedStudentRecordAdmin(admin.ModelAdmin):
    list_display = ('enrollment_number', 'student_name', 'department', 'semester', 'verification_code', 'is_registered', 'mobile')
    list_filter = ('department', 'semester', 'is_registered')
    search_fields = ('enrollment_number', 'student_name', 'verification_code', 'mobile')

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('dp_preview', 'user', 'verified_record')
    search_fields = ('user__username', 'verified_record__student_name')

    def dp_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="40" height="40" style="object-fit:cover; border-radius:50%; border:2px solid #3b82f6;" />', obj.photo.url)
        return "No DP"
    dp_preview.short_description = "Profile DP"

@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ('dp_preview', 'teacher_id', 'full_name', 'department', 'designation', 'mobile')
    list_filter = ('department',)
    search_fields = ('teacher_id', 'full_name')
    fields = ('user', 'teacher_id', 'full_name', 'department', 'designation', 'mobile', 'photo')

    def dp_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="40" height="40" style="object-fit:cover; border-radius:50%; border:2px solid #10b981;" />', obj.photo.url)
        return "No DP"
    dp_preview.short_description = "Teacher DP"

class StudentAttendanceItemInline(admin.TabularInline):
    model = StudentAttendanceItem
    extra = 0
    can_delete = False

@admin.register(AttendanceSession)
class AttendanceSessionAdmin(admin.ModelAdmin):
    list_display = ('department', 'semester', 'subject_name', 'date', 'taken_by')
    list_filter = ('department', 'semester', 'date')
    inlines = [StudentAttendanceItemInline]
