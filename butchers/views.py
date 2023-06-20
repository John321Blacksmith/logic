from rest_framework import viewsets
from .models import Meat
from .serializers import MeatSerializer

# Create your views here.

class MeatViewSet(viewsets.ModelViewSet):
	queryset = Meat.objects.all()
	serializer_class = MeatSerializer
