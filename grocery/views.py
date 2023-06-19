from rest_framework import generics
from .models import Vegetable, Fruit
from .serializers import VegetableSerializer, FruitSerializer

# Create your views here.

class VegetableList(generics.ListCreateAPIView):
	queryset = Vegetable.objects.all()
	serializer_class = VegetableSerializer


class VegetableDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Vegetable.objects.all()
	serializer_class = VegetableSerializer


class FruitList(generics.ListCreateAPIView):
	queryset = Fruit.objects.all()
	serializer_class = FruitSerializer


class FruitDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Fruit.objects.all()
	serializer_class = FruitSerializer
