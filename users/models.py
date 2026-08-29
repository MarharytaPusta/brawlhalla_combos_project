from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from game_db.models import Weapon, Combo


class User(AbstractUser):
    picture = models.ImageField(upload_to='brawlhalla_static/images/legends_images/', null=True, blank=True)


class UserComboWeapon(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='saved_combos')
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE, related_name='user_combos')


class ComboStep(models.Model):
    user_combo = models.ForeignKey(UserComboWeapon, on_delete=models.CASCADE, related_name='steps')
    combo = models.ForeignKey(Combo, on_delete=models.CASCADE)
    step_order = models.IntegerField()

    class Meta:
        ordering = ['step_order']