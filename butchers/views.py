from rest_framework import generics
from .models import Meat
from .serializers import MeatSerializer

# Create your views here.

class MeatList(generics.ListCreateAPIView):
	queryset = Meat.objects.all()
	serializer_class = MeatSerializer


class MeatDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Meat.objects.all()
	serializer_class = MeatSerializer