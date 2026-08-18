import yaml
from game_db.models import Button


def load_buttons_from_yaml(file_name: str) -> None:
    with open(file_name, 'r') as file:
        buttons_data = yaml.safe_load(file)

        for item in buttons_data:
            button, _ = Button.objects.get_or_create(
                name=item['name'],
                defaults={'picture': item['picture']}
            )