from django.urls import path, include
from rest_framework import routers
from .views import BreadViewSet


router = routers.DefaultRouter()
router.register(r'', BreadViewSet)


app_name = 'bakery'
urlpatterns = [
	path('', include(router.urls)),
]