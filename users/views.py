from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm

from .forms import CustomUserCreationForm
from game_db.models import Weapon
from .models import User, UserComboWeapon, AttackStep


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


def user_combos(request):
    weapon_combos = {}

    user = request.user

    user_weapons = UserComboWeapon.objects.filter(user=user)
    lst = []
    for user_weapon in user_weapons:
        weapon = user_weapon.weapon
        attack_steps = AttackStep.objects.filter(user_combo=user_weapon)
        attack_steps = [attack_step.attack.name for attack_step in attack_steps]
        attack_steps = ' ➔ '.join(attack_steps)
        lst.append(attack_steps)
        weapon_combos[weapon.name] = lst

    dict_values = {"weapon_combos" : weapon_combos}
    print(dict_values)

    return render(request, 'user_templates/user_combos.html', dict_values)