from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import json

from game_db.models import Legend, Combo, Button, Attack, AttackButton


def all_legends(request) -> HttpResponse:
    legends = Legend.objects.all()
    legends = legends.order_by('name')
    dict_of_values = {
        "legends" : legends,
    }
    return render(request,'character_templates/choose_legend.html', dict_of_values)


def get_attacks_buttons() -> dict[str, list[str]]:
    dict_buttons_to_attack = {}
    attacks = Attack.objects.all()
    for attack in attacks:
        buttons = AttackButton.objects.filter(attack = attack)
        buttons = buttons.order_by('order')
        buttons = [button.button for button in buttons]
        buttons = [button.name for button in buttons]
        buttons = " ➔ ".join(buttons)
        dict_buttons_to_attack[attack.name] = buttons
    return dict_buttons_to_attack


def get_buttons_pictures() -> dict[str, str]:
    buttons = Button.objects.all()
    dict_buttons_pictures = {}
    for button in buttons:
        dict_buttons_pictures[button.name] = button.picture.name
    return dict_buttons_pictures


def get_all_legend_info(request, legend_name) -> HttpResponse:
    dict_buttons_to_attack = get_attacks_buttons()
    json_buttons_to_attack = json.dumps(dict_buttons_to_attack)
    dict_buttons_pictures = get_buttons_pictures()
    json_buttons_pictures = json.dumps(dict_buttons_pictures)
    legend = get_object_or_404(Legend, name=legend_name)
    weapons = legend.weapons.all()
    first_weapon = weapons[0]
    second_weapon = weapons[1]
    combos_for_weapon_1 = Combo.objects.filter(weapon=first_weapon)
    combos_for_weapon_2 = Combo.objects.filter(weapon=second_weapon)

    dict_of_values = {
        "legend_name" : legend.name,
        "legend_picture" : legend.picture,
        "weapon1" : first_weapon.name,
        "combos1" : combos_for_weapon_1,
        "weapon2" : second_weapon.name,
        "combos2" : combos_for_weapon_2,
        "json_buttons_to_attack" : json_buttons_to_attack,
        "json_buttons_pictures" : json_buttons_pictures,
    }

    return render(request,'character_templates/legend.html', dict_of_values)