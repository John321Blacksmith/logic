from django.urls import path, include
from rest_framework import routers
from .views import MeatViewSet


router = routers.DefaultRouter()
router.register(r'', MeatViewSet)


app_name = 'butchers'
urlpatterns = [
	path('', include(router.urls)),
]