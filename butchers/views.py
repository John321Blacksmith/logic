from rest_framework import generics
from .models import Meat
from .serializers MealSerializer

# Create your views here.

class MeatList(generics.ListCreateAPIView):
	queryset = Meat.objects.all()
	serializer_class = MealSerializer


class MeatDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Meat.objects.all()
	serializer_class = MealSerializer