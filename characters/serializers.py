from rest_framework import serializers

class ComboSerializer(serializers.Serializer):
    combo = serializers.CharField()

    def validate_combo(self, value):
        weapon_index = value.find(':')
        weapon = value[:weapon_index - 9]
        weapon = weapon.strip()
        value = value[weapon_index + 2:]
        parts = value.split('➔')
        parts = [p.strip() for p in parts]
        dict_weapon_combo = {"weapon" : weapon,
                             "combos" : parts}
        return dict_weapon_combo