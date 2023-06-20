from rest_framework import viewsets
from .models import Vegetable, Fruit
from .serializers import VegetableSerializer, FruitSerializer

# Create your views here.

class VegetableViewSet(viewsets.ModelViewSet):
	queryset = Vegetable.objects.all()
	serializer_class = VegetableSerializer


class FruitViewSet(viewsets.ModelViewSet):
	queryset = Fruit.objects.all()
	serializer_class = FruitSerializer

