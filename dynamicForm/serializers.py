from rest_framework import serializers
from .models import FormField, Options

class OptionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = ['id', 'name']

class FormFieldSerializer(serializers.ModelSerializer):
    options = OptionsSerializers(many=True)

    class Meta:
        model = FormField
        fields = [
            'id',
            'label',
            'name',
            'field',
            'requiredYn',
            'errorMessage',
            'inline',
            'toasterMessage',
            'options'
        ]

    def create(self, validated_data):
        options_data = validated_data.pop('options', [])
        form_field = FormField.objects.create(**validated_data)
        for opt in options_data:
            option, _ = Options.objects.get_or_create(**opt)
            form_field.options.add(option)
        return form_field

    def update(self, instance, validated_data):
        options_data = validated_data.pop('options', [])
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Update related options
        if options_data:
            instance.options.clear()
            for opt in options_data:
                option, _ = Options.objects.get_or_create(**opt)
                instance.options.add(option)
        return instance