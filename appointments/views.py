from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.decorators import role_required
from accounts.models import User
from .models import Appointment
from .forms import AppointmentForm
from patients.models import Patient


# ✅ List Appointments
@login_required
def appointment_list(request):
    if request.user.role == 'doctor':
        appointments = Appointment.objects.filter(doctor=request.user)
    else:
        appointments = Appointment.objects.filter(patient__user=request.user)

    return render(request, 'appointments/list.html', {'appointments': appointments})


# ✅ Create Appointment (Patient books)
@login_required
@role_required('patient')
def appointment_create(request):
    form = AppointmentForm(request.POST or None, exclude_patient=True)

    if form.is_valid():
        appointment = form.save(commit=False)

        # Set patient to current user's patient profile
        appointment.patient = Patient.objects.get(user=request.user)

        # Assign first available doctor
        doctor = User.objects.filter(role='doctor').first()
        appointment.doctor = doctor

        # 🔥 Conflict check
        conflict = Appointment.objects.filter(
            doctor=appointment.doctor,
            date=appointment.date,
            start_time__lt=appointment.end_time,
            end_time__gt=appointment.start_time
        ).exists()

        if conflict:
            form.add_error(None, "This time slot is already booked!")
        else:
            appointment.save()
            return redirect('appointment_list')

    return render(request, 'appointments/create.html', {'form': form})


# ✅ Update Appointment (Doctor Only)
@login_required
@role_required('doctor')
def appointment_update(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk, doctor=request.user)

    form = AppointmentForm(request.POST or None, instance=appointment)

    if form.is_valid():
        form.save()
        return redirect('appointment_list')

    return render(request, 'appointments/update.html', {'form': form})


# ✅ Delete Appointment
@login_required
def appointment_delete(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)

    if request.method == "POST":
        appointment.delete()
        return redirect('appointment_list')

    return render(request, 'appointments/delete.html', {'appointment': appointment})
