import yaml
from characters_db.models import Attack, Combo, ComboAttack, Weapon


def get_attacks(attacks_names : list[str]) -> list[Attack]:
    attacks = []
    for name in attacks_names:
        attack = Attack.objects.get(name=name)
        attacks.append(attack)
    return attacks


def connect_combos_with_attacks(combo, attacks) -> None:
    for i in range(len(attacks)):
        combo_attack , _ = ComboAttack.objects.get_or_create(
            combo = combo,
            attack = attacks[i],
            order = i + 1
        )


def load_combos_from_yaml_to_db(file_name: str) -> None:
    with open(file_name, 'r') as file:
        combos_data = yaml.safe_load(file)

        Combo.objects.all().delete()

        for item in combos_data:
            attack_names = item["attacks"]
            attacks = get_attacks(attack_names)
            weapon_name = item["weapon"]
            weapon = Weapon.objects.get(name = weapon_name)
            combo = Combo.objects.create(weapon = weapon)
            connect_combos_with_attacks(combo, attacks)