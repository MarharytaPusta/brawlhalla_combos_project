from django.db import models

class Weapon(models.Model):
    name = models.CharField(max_length=20, unique=True)


class Legend(models.Model):
    name = models.CharField(max_length=50, unique=True)
    picture = models.ImageField(upload_to='brawlhalla_static/images/legends/', null=True, blank=True)

    weapons = models.ManyToManyField(Weapon, related_name='legends')


class Button(models.Model):
    name = models.CharField(max_length=50, unique=True)
    picture = models.ImageField(upload_to='brawlhalla_static/images/buttons/')


class Attack(models.Model):
    name = models.CharField(max_length=200, unique=True)

    buttons = models.ManyToManyField(Button, through='AttackButton')


class Combo(models.Model):

    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE, related_name='combos')

    attacks = models.ManyToManyField(Attack, through='ComboAttack')


    def get_all_attacks(self):
        steps = ComboAttack.objects.filter(combo=self)

        steps_with_attacks = steps.select_related('attack')

        sorted_steps = steps_with_attacks.order_by('order')

        attack_names = []
        for step in sorted_steps:
            attack_names.append(step.attack.name)

        return " ➔ ".join(attack_names)


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
