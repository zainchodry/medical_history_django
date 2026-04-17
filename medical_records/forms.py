from django import forms
from .models import MedicalRecord, MedicalAttachment


class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['patient', 'record_type', 'title', 'diagnosis', 'treatment', 'notes', 'visit_date']
        widgets = {
            'patient': forms.Select(attrs={
                'class': 'form-select'
            }),
            'record_type': forms.Select(attrs={
                'class': 'form-select'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter record title'
            }),
            'diagnosis': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter diagnosis details',
                'rows': 3
            }),
            'treatment': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter treatment details',
                'rows': 3
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Additional notes (optional)',
                'rows': 3
            }),
            'visit_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }


class AttachmentForm(forms.ModelForm):
    class Meta:
        model = MedicalAttachment
        fields = ['file']
        widgets = {
            'file': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }