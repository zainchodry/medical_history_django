from django.db import models
from django.conf import settings
from patients.models import Patient

User = settings.AUTH_USER_MODEL


class MedicalRecord(models.Model):
    RECORD_TYPES = (
        ('consultation', 'Consultation'),
        ('diagnosis', 'Diagnosis'),
        ('lab', 'Lab Report'),
        ('surgery', 'Surgery'),
    )

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='records')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)

    record_type = models.CharField(max_length=20, choices=RECORD_TYPES)

    title = models.CharField(max_length=255)
    diagnosis = models.TextField(blank=True)
    treatment = models.TextField(blank=True)
    notes = models.TextField(blank=True)

    visit_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class MedicalAttachment(models.Model):
    record = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='medical_records/')