from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .models import User, UserComboWeapon, AttackStep

class CustomUserAdmin(UserAdmin):
    model = User

    fieldsets = UserAdmin.fieldsets + (
        ('Additional info', {'fields': ('picture',)}),
    )

admin.site.register(User, CustomUserAdmin)

admin.site.register(UserComboWeapon)
admin.site.register(AttackStep)
