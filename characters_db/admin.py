from django.contrib import admin
from .models import Weapon, Character, Button, Attack, Combo, ComboAttack, AttackButton

admin.site.register(Weapon)
admin.site.register(Character)
admin.site.register(Button)
admin.site.register(Attack)
admin.site.register(Combo)

admin.site.register(ComboAttack)
admin.site.register(AttackButton)