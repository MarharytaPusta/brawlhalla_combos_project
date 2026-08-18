import requests

from game_db.models import Legend, Weapon

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
            legends_info = data.get("legends", [])
            for legend_info in legends_info:
                try:
                    legend = create_legend_in_db(legend_info)
                    create_weapon_in_db(legend, legend_info, "weapon_one")
                    create_weapon_in_db(legend, legend_info, "weapon_two")
                except:
                    continue


def create_legend_in_db(legend_info : dict) -> Legend:
    name = legend_info.get("bio_name")
    if not name:
        raise ValueError
    legend, _ = Legend.objects.get_or_create(name=name, defaults={'picture': ''})
    return legend


def get_correct_weapon_name(weapon_name : str) -> str | None:
    if not weapon_name:
        return None
    if weapon_name in weapon_fixed_names:
        return weapon_fixed_names[weapon_name]
    else:
        return weapon_name


def create_weapon_in_db(legend : Legend, legend_info : dict, name_of_weapon : str) -> None:
    weapon = legend_info.get(name_of_weapon)
    weapon = get_correct_weapon_name(weapon)
    if weapon:
        weapon1, _ = Weapon.objects.get_or_create(name=weapon)
        legend.weapons.add(weapon1)


def get_legends(url : str) -> None:
    response = connect_to_api(url)
    if response is not None:
        fetch_all_legends_info(response)
