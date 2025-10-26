from rest_framework import serializers
from .models import BOMSettings, UOM

class UOMSerializers(serializers.ModelSerializer):
    class Meta:
        model = UOM
        fields = '__all__'

class BOMSettingsSerializers(serializers.ModelSerializer):
    DefaultUOM = UOMSerializers(read_only=True)
    DefaultUOM_id = serializers.PrimaryKeyRelatedField(
        queryset=UOM.objects.all(),
        source='DefaultUOM',
        write_only=True,
        required=False
    )

    class Meta:
        model = BOMSettings
        fields = '__all__'

    def create(self, validated_data):
        return BOMSettings.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
