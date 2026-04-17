from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.decorators import role_required
from .models import Prescription, Medicine
from .forms import PrescriptionForm, MedicineForm
from patients.models import Patient


# ✅ List Prescriptions
@login_required
@role_required('doctor')
def prescription_list(request):
    prescriptions = Prescription.objects.filter(doctor=request.user)
    return render(request, 'prescriptions/list.html', {'prescriptions': prescriptions})


# ✅ Create Prescription
@login_required
@role_required('doctor')
def prescription_create(request):
    form = PrescriptionForm(request.POST or None)

    # Only doctor's patients
    form.fields['patient'].queryset = Patient.objects.filter(user=request.user)

    if request.method == "POST" and form.is_valid():
        prescription = form.save(commit=False)
        prescription.doctor = request.user
        prescription.save()

        # 🔥 Multiple medicines
        names = request.POST.getlist('name')
        dosages = request.POST.getlist('dosage')
        frequencies = request.POST.getlist('frequency')
        durations = request.POST.getlist('duration')

        for i in range(len(names)):
            Medicine.objects.create(
                prescription=prescription,
                name=names[i],
                dosage=dosages[i],
                frequency=frequencies[i],
                duration=durations[i],
            )

        return redirect('prescription_list')

    return render(request, 'prescriptions/create.html', {'form': form})


# ✅ Detail View
@login_required
def prescription_detail(request, pk):
    prescription = get_object_or_404(Prescription, pk=pk)
    return render(request, 'prescriptions/detail.html', {'prescription': prescription})


# ✅ Delete
@login_required
@role_required('doctor')
def prescription_delete(request, pk):
    prescription = get_object_or_404(Prescription, pk=pk, doctor=request.user)

    if request.method == "POST":
        prescription.delete()
        return redirect('prescription_list')

    return render(request, 'prescriptions/delete.html', {'prescription': prescription})