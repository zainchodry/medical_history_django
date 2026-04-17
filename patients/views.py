from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.decorators import role_required
from .models import Patient
from .forms import PatientForm

@login_required
@role_required('doctor')
def patient_list(request):
    patients = Patient.objects.filter(user=request.user)
    return render(request, 'patients/list.html', {'patients': patients})

@login_required
@role_required('doctor')
def patient_create(request):
    form = PatientForm(request.POST or None)

    if form.is_valid():
        patient = form.save(commit=False)
        patient.user = request.user
        patient.save()
        return redirect('patient_list')

    return render(request, 'patients/create.html', {'form': form})

@login_required
@role_required('doctor')
def patient_update(request, pk):
    patient = get_object_or_404(Patient, pk=pk, user=request.user)
    form = PatientForm(request.POST or None, instance=patient)

    if form.is_valid():
        form.save()
        return redirect('patient_list')

    return render(request, 'patients/update.html', {'form': form})

@login_required
@role_required('doctor')
def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk, user=request.user)

    if request.method == "POST":
        patient.delete()
        return redirect('patient_list')

    return render(request, 'patients/delete.html', {'patient': patient})

@login_required
@role_required('patient')
def my_profile(request):
    patient = Patient.objects.filter(user=request.user).first()
    return render(request, 'patients/my_profile.html', {'patient': patient})