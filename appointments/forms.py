from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        exclude_patient = kwargs.pop('exclude_patient', False)
        super().__init__(*args, **kwargs)

        if exclude_patient:
            # Remove patient field for patients creating appointments
            del self.fields['patient']

    class Meta:
        model = Appointment
        fields = ['patient', 'date', 'start_time', 'end_time', 'notes']
        widgets = {
            'patient': forms.Select(attrs={
                'class': 'form-select'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control flatpickr-date',
                'type': 'text',
                'placeholder': 'Select date'
            }),
            'start_time': forms.TimeInput(attrs={
                'class': 'form-control flatpickr-time',
                'type': 'text',
                'placeholder': 'Select start time'
            }),
            'end_time': forms.TimeInput(attrs={
                'class': 'form-control flatpickr-time',
                'type': 'text',
                'placeholder': 'Select end time'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter appointment notes (optional)',
                'rows': 3
            }),
        }