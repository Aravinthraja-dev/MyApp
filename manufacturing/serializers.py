from rest_framework import serializers
from .models import Product
from configurations.models import UOM

class ProductSerializers(serializers.ModelSerializer):
    UOM_id = serializers.PrimaryKeyRelatedField(
        queryset=UOM.objects.all(),
        source='UOM',
        write_only=True,
        required=False
    )
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

