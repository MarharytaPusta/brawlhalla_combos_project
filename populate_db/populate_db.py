import sys
import os
import django

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Brawlhalla_combos_website.settings')
django.setup()

from get_characters_and_weapons import get_legends
from get_buttons import load_buttons_from_yaml
from get_attacks import load_attacks_from_yaml_to_db
from get_combos import load_combos_from_yaml_to_db
from add_images_to_legends import connect_image_to_legend

if __name__ == "__main__":
    get_legends("https://api.brawlhalla.com/v1/static/legends")
    load_buttons_from_yaml("data_fo_db/buttons.yaml")
    load_attacks_from_yaml_to_db("data_fo_db/attacks.yaml")
    load_combos_from_yaml_to_db("data_fo_db/combos.yaml")
    connect_image_to_legend()
