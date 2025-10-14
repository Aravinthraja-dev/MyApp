from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FormFieldViewSet, OptionsViewSet

router = DefaultRouter()
router.register(r'formfields', FormFieldViewSet)
router.register(r'options', OptionsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
