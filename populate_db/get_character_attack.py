import requests

from characters_db.models import Character, Weapon

weapon_fixed_names = {
    "Fists": "Gauntlets",
    "Pistol": "Blasters",
    "RocketLance": "Rocket Lance",
    "Katar" : "Katars"
}

def connect_to_api(url : str) -> requests.Response:
    params = {
        "max_results" : 100
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response
    except requests.RequestException as e:
        print(f"Помилка підключення до API: {e}")
        return None


def fetch_all_legends_info(response : requests.Response) -> None:
    if response is not None:
        if response.status_code == 200:
            data = response.json()
            characters_info = data.get("legends", [])
            for character_info in characters_info:
                try:
                    character = create_character_in_db(character_info)
                    create_weapon_in_db(character, character_info, "weapon_one")
                    create_weapon_in_db(character, character_info, "weapon_two")
                except:
                    continue


def create_character_in_db(character_info : dict) -> Character:
    name = character_info.get("bio_name")
    if not name:
        raise ValueError
    character, _ = Character.objects.get_or_create(name=name, defaults={'pic_url': ''})
    return character


def get_correct_weapon_name(weapon_name : str) -> str | None:
    if not weapon_name:
        return None
    if weapon_name in weapon_fixed_names:
        return weapon_fixed_names[weapon_name]
    else:
        return weapon_name


def create_weapon_in_db(character : Character, character_info : dict, name_of_weapon : str) -> None:
    weapon = character_info.get(name_of_weapon)
    weapon = get_correct_weapon_name(weapon)
    if weapon:
        weapon1, _ = Weapon.objects.get_or_create(name=weapon)
        character.weapons.add(weapon1)


def get_characters(url : str) -> None:
    response = connect_to_api(url)
    if response is not None:
        fetch_all_legends_info(response)
