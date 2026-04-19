from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.decorators import role_required
from .models import MedicalRecord, MedicalAttachment
from .forms import MedicalRecordForm, AttachmentForm
from patients.models import Patient


# ✅ List Records (Timeline 🔥)
@login_required
@role_required('doctor')
def record_list(request):
    records = MedicalRecord.objects.filter(doctor=request.user).order_by('-visit_date')
    return render(request, 'medical_records/list.html', {'records': records})


# ✅ Create Record
@login_required
@role_required('doctor')
def record_create(request):
    form = MedicalRecordForm(request.POST or None)

    # Only show doctor's patients
    form.fields['patient'].queryset = Patient.objects.filter(
    appointment__doctor=request.user
    ).distinct()

    if form.is_valid():
        record = form.save(commit=False)
        record.doctor = request.user
        record.save()
        return redirect('record_list')

    return render(request, 'medical_records/create.html', {'form': form})


# ✅ Detail View (with attachments)
@login_required
def record_detail(request, pk):
    record = get_object_or_404(MedicalRecord, pk=pk)

    form = AttachmentForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        attachment = form.save(commit=False)
        attachment.record = record
        attachment.save()
        return redirect('record_detail', pk=pk)

    return render(request, 'medical_records/detail.html', {
        'record': record,
        'form': form
    })


# ✅ Delete Record
@login_required
@role_required('doctor')
def record_delete(request, pk):
    record = get_object_or_404(MedicalRecord, pk=pk, doctor=request.user)

    if request.method == "POST":
        record.delete()
        return redirect('record_list')

    return render(request, 'medical_records/delete.html', {'record': record})