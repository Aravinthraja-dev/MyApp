from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import BOMSettings, UOM
from .serializers import BOMSettingsSerializers, UOMSerializers

class BOMSettingsViewSet(viewsets.ModelViewSet):
    queryset = BOMSettings.objects.all()
    serializer_class = BOMSettingsSerializers

    def create(self, request, *args, **kwargs):
        existing = BOMSettings.objects.first()
        if existing:
            serializer = self.get_serializer(existing, data=request.data, partial=True)
        else:
            serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class UOMViewSet(viewsets.ModelViewSet):
    queryset = UOM.objects.all()
    serializer_class = UOMSerializers
