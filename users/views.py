from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles import finders
from django.conf import settings
import json
import os

from .forms import CustomUserCreationForm
from .models import UserComboWeapon, AttackStep
from characters.views import get_attacks_buttons, get_buttons_pictures


def register(request) -> HttpResponse:
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('../profile')
    else:
        form = CustomUserCreationForm()

    return render(request,'user_templates/register.html', {'form': form})


def login(request) -> HttpResponse:
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('../profile')
    else:
        form = AuthenticationForm()

    return render(request,'user_templates/login.html', {'form': form})


def user_combos(request) -> HttpResponse:
    if request.method == "POST":
        return delete_combo(request)

    weapon_combos = {}

    user = request.user

    user_weapons = UserComboWeapon.objects.filter(user=user)
    for user_weapon in user_weapons:
        user_attack_id = user_weapon.id
        attack_and_id = [user_attack_id]
        weapon = user_weapon.weapon
        attack_steps = AttackStep.objects.filter(user_combo=user_weapon)
        attack_steps = [attack_step.attack.name for attack_step in attack_steps]
        attack_steps = ' ➔ '.join(attack_steps)
        attack_and_id.append(attack_steps)
        if weapon.name in weapon_combos:
            weapon_combos[weapon.name].append(attack_and_id)
        else:
            weapon_combos[weapon.name] = [attack_and_id]

    dict_buttons_to_attack = get_attacks_buttons()
    json_buttons_to_attack = json.dumps(dict_buttons_to_attack)
    dict_buttons_pictures = get_buttons_pictures()
    json_buttons_pictures = json.dumps(dict_buttons_pictures)

    dict_values = {"weapon_combos" : weapon_combos,
                   "json_buttons_to_attack": json_buttons_to_attack,
                   "json_buttons_pictures": json_buttons_pictures,
                   }

    return render(request, 'user_templates/user_combos.html', dict_values)


def delete_combo(request):
    try:
        data = json.loads(request.body)
        item_id = data.get("item_id")
        item = UserComboWeapon.objects.get(id=item_id)
        item.delete()
        return HttpResponse("success")

    except Exception:
        return HttpResponse("error", status=400)


@login_required
def profile(request) -> HttpResponse:
    user = request.user

    if request.method == 'POST':
        selected_avatar = request.POST.get('selected_avatar')
        if selected_avatar:
            user.picture = selected_avatar
            user.save()

    legends_dir = os.path.join(settings.BASE_DIR, 'brawlhalla_static', 'images', 'legends_images')
    legends_pictures = []
    relative_folder_path = 'brawlhalla_static/images/legends_images'
    absolute_path = finders.find(relative_folder_path)

    if absolute_path and os.path.exists(absolute_path):
        for file in os.listdir(absolute_path):
            if file.lower().endswith('.webp'):
                legends_pictures.append(f'{relative_folder_path}/{file}')

    return render(request, 'user_templates/profile.html', {
        'user': user,
        'legends_photos': legends_pictures
    })


def logout(request):
    auth_logout(request)
    return redirect('/')