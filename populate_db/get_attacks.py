import yaml
from game_db.models import Attack, Button, AttackButton


def get_buttons(button_names : list[str]) -> list[Button]:
    buttons = []
    for button_name in button_names:
        button = Button.objects.get(name=button_name)
        buttons.append(button)
    return buttons


def connect_attack_with_buttons(attack, buttons) -> None:
    for i in range(len(buttons)):
        attack_button, _ = AttackButton.objects.get_or_create(
            attack=attack,
            button=buttons[i],
            order=i + 1
        )


def load_attacks_from_yaml_to_db(file_name: str) -> None:
    with open(file_name, 'r') as file:
        attacks_data = yaml.safe_load(file)

        for item in attacks_data:
            button_names = item['buttons']
            buttons = get_buttons(button_names)

            attack, _ = Attack.objects.get_or_create(name=item['name'])

            connect_attack_with_buttons(attack, buttons)