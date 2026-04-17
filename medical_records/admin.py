from django.contrib import admin
from .models import MedicalRecord, MedicalAttachment


@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('title', 'patient', 'doctor', 'record_type', 'visit_date')
    list_filter = ('record_type', 'visit_date')
    search_fields = ('title', 'patient__full_name')


@admin.register(MedicalAttachment)
class MedicalAttachmentAdmin(admin.ModelAdmin):
    list_display = ('record', 'file')
