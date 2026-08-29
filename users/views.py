from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm

from .forms import CustomUserCreationForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('../profile')
    else:
        form = CustomUserCreationForm()

    return render(request,'user_templates/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('../profile')
    else:
        form = AuthenticationForm()

    return render(request,'user_templates/login.html', {'form': form})


def profile(request):
    return render(request, 'user_templates/profile.html')