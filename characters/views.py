from django.shortcuts import render

def combos(request):
    return render(request,'character_templates/character.html')