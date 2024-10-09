# main_fns_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, CustomLoginForm, CustomPasswordChangeForm
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy


# User Registration
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'main_fns_app/register.html', {'form': form})

# Custom Login View
class CustomLoginView(LoginView):
    authentication_form = CustomLoginForm
    template_name = 'main_fns_app/login.html'

# Custom Password Change View
class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    success_url = reverse_lazy('password_change_done')
    template_name = 'main_fns_app/password_change.html'

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')

# Dashboard (protected for logged-in users)
@login_required
def dashboard(request):
    return render(request, 'main_fns_app/dashboard.html')


