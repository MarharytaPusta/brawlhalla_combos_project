import requests

from game_db.models import Legend


def get_image_name(legend_name : str, file_type : str = "webp") -> str:
    legend_name = legend_name.replace(" ", "_")
    image_name = legend_name.replace(" ", "_")
    image_name = f"{image_name}.{file_type}"
    return image_name


def connect_image_to_legend() -> None:
    image_parents = "brawlhalla_static/images/legends_images"
    legends = Legend.objects.all()

    for legend in legends:
        legend_name = legend.name
        image_name = get_image_name(legend_name)
        image_path = f"{image_parents}/{image_name}"
        legend.picture = image_path
        legend.save()