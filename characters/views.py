from django.shortcuts import render, get_object_or_404

from game_db.models import Legend, Weapon, Combo, ComboAttack



def all_legends(request):
    legends = Legend.objects.all()
    legends = legends.order_by('name')
    dict_of_values = {
        "legends" : legends,
    }
    return render(request,'character_templates/choose_legend.html', dict_of_values)


def get_all_legend_info(request, legend_name):
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
    }

    return render(request,'character_templates/legend.html', dict_of_values)