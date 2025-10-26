from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BOMSettingsViewSet, UOMViewSet

router = DefaultRouter()
router.register(f'configrations', BOMSettingsViewSet)
router.register(f'uom', UOMViewSet)

urlpatterns = [
    path('', include(router.urls)),
]