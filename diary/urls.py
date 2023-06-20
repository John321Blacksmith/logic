from django.urls import path, include
from .views import MilkViewSet, KefirViewSet, CheeseViewSet, CabbCheeseViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'milk', MilkViewSet, basename='milk')
router.register(r'kefir', KefirViewSet, basename='kefir')
router.register(r'cheese', CheeseViewSet, basename='cheese')
router.register(r'cabb-cheese', CabbCheeseViewSet, basename='cabb-cheese')

app_name = 'diary'

urlpatterns = [
	path('diary/', include(router.urls)),
]
