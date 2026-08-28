from django.shortcuts import render

def register(request):
    return render(request,'user_templates/register.html')

def login(request):
    return render(request,'user_templates/login.html')

def profile(request):
    user_info = {"email" : "name_surname@gmail.com",
                 "picture_path" : r"brawlhalla_static\images\legends_images\Yumiko.webp"}
    return render(request,'user_templates/profile.html', user_info)