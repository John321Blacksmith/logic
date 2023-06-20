from django.urls import path, include
from rest_framework import routers
from .views import VegetableViewSet, FruitViewSet


router = routers.DefaultRouter()
router.register(r'vegetables', VegetableViewSet)
router.register(r'fruits', FruitViewSet)


app_name = 'grocery'
urlpatterns = [
	path('', include(router.urls)),
]