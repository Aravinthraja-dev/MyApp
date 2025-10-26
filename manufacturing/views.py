from rest_framework import viewsets
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializers

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    def create(self, request, *args, **kwargs):
        serializers = self.get_serializer(data=request.data)
        if not serializers.is_valid():
            print(serializers.errors)
            return Response(serializers.errors, status=400)
        return super().create(request, *args, *kwargs)
