from rest_framework import viewsets
from .models import Bread
from .serializers import BreadSerializer

# Create your views here.

class BreadViewSet(viewsets.ModelViewSet):
	queryset = Bread.objects.all()
	serializer_class = BreadSerializer
