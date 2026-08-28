from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
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
    return render(request,'user_templates/login.html')

def profile(request):
    user_info = {"email" : "name_surname@gmail.com",
                 "picture_path" : r"brawlhalla_static\images\legends_images\Yumiko.webp"}
    return render(request,'user_templates/profile.html', user_info)