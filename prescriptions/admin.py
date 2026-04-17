from django.contrib import admin
from .models import Prescription, Medicine


@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('patient__full_name',)


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'prescription', 'dosage', 'frequency', 'duration')
    search_fields = ('name',)
