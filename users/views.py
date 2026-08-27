from django.shortcuts import render

def register(request):
    return render(request,'user_templates/register.html')

def login(request):
    return render(request,'user_templates/login.html')