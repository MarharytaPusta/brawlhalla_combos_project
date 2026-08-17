import requests

from characters_db.models import Character, Weapon


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
                    create_weapons_in_db(character, character_info)
                except:
                    continue


def create_character_in_db(character_info : dict) -> Character:
    name = character_info.get("bio_name")
    if not name:
        raise ValueError
    character, _ = Character.objects.get_or_create(name=name, defaults={'pic_url': ''})
    return character


def create_weapons_in_db(character : Character, character_info : dict) -> None:
    weapon1 = character_info.get("weapon_one")
    weapon2 = character_info.get("weapon_two")
    weapon1, _ = Weapon.objects.get_or_create(name=weapon1)
    weapon2, _ = Weapon.objects.get_or_create(name=weapon2)
    character.weapons.add(weapon1)
    character.weapons.add(weapon2)


def get_characters(url : str) -> None:
    response = connect_to_api(url)
    if response is not None:
        fetch_all_legends_info(response)
        Weapon.objects.filter(name = "Fists").update(name = "Gauntlets")


if __name__ == "__main__":
    get_characters()