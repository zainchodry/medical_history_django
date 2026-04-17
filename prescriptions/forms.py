from django import forms
from .models import Prescription, Medicine


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['patient', 'medical_record', 'notes']
        widgets = {
            'patient': forms.Select(attrs={
                'class': 'form-select'
            }),
            'medical_record': forms.Select(attrs={
                'class': 'form-select'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter prescription notes (optional)',
                'rows': 3
            }),
        }


class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name', 'dosage', 'frequency', 'duration', 'instructions']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Medicine name'
            }),
            'dosage': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. 500mg'
            }),
            'frequency': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Twice a day'
            }),
            'duration': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. 5 days'
            }),
            'instructions': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Special instructions (after meal, before sleep, etc.)',
                'rows': 3
            }),
        }