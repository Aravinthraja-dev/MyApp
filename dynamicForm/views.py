from rest_framework import viewsets
from .models import FormField, Options
from .serializers import FormFieldSerializer, OptionsSerializers



class OptionsViewSet(viewsets.ModelViewSet):
    queryset = Options.objects.all()
    serializer_class = OptionsSerializers


class FormFieldViewSet(viewsets.ModelViewSet):
    queryset = FormField.objects.all()
    serializer_class = FormFieldSerializer
