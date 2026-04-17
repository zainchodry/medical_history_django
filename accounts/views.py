from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Profile
from .forms import ChangePasswordForm, ProfileForm


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'accounts/dashboard.html')


class Register_view:
    """Class-based register view using Django's View."""
    from django.views import View


from django.views import View


class Register_view(View):
    def get(self, request):
        from .forms import RegisterForm
        form = RegisterForm()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        from .forms import RegisterForm
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
        return render(request, 'accounts/register.html', {'form': form})


def logout(request):
    auth_logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')


@login_required
def password_change_view(request):
    form = ChangePasswordForm(request.user)
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password has been changed successfully.')
            return redirect('dashboard')
    return render(request, 'accounts/password_change.html', {'form': form})


@login_required
def profile_view(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    return render(request, 'accounts/profile.html', {'form': form})