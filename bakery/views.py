from rest_framework import generics
from .models import Bread
from .serializers import BreadSerializer

# Create your views here.

class BreadList(generics.ListCreateAPIView):
	queryset = Bread.objects.all()
	serializer_class = BreadSerializer

	
class BreadDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Bread.objects.all()
	serializer_class = BreadSerializer