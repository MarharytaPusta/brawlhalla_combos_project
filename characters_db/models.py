from django.db import models

class Weapon(models.Model):
    name = models.CharField(max_length=20, unique=True)


class Character(models.Model):
    name = models.CharField(max_length=50, unique=True)
    picture = models.ImageField(upload_to='character_static/images/legends/', null=True, blank=True)

    weapons = models.ManyToManyField(Weapon, related_name='characters')


class Button(models.Model):
    name = models.CharField(max_length=50, unique=True)
    picture = models.ImageField(upload_to='character_static/images/buttons/')


class Attack(models.Model):
    name = models.CharField(max_length=200, unique=True)

    buttons = models.ManyToManyField(Button, through='AttackButton')


class Combo(models.Model):

    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE, related_name='combos')

    attacks = models.ManyToManyField(Attack, through='ComboAttack')


class ComboAttack(models.Model):
    combo = models.ForeignKey(Combo, on_delete=models.CASCADE)
    attack = models.ForeignKey(Attack, on_delete=models.CASCADE)
    order = models.IntegerField()

    class Meta:
        ordering = ['order']


class AttackButton(models.Model):
    attack = models.ForeignKey(Attack, on_delete=models.CASCADE)
    button = models.ForeignKey(Button, on_delete=models.CASCADE)
    order = models.IntegerField()

    class Meta:
        ordering = ['order']
