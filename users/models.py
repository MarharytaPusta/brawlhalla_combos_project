from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    picture = models.ImageField(upload_to='brawlhalla_static/images/legends/', null=True, blank=True)