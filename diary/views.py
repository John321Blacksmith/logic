from rest_framework import viewsets
from .models import Milk, Kefir, Cheese, CabbageCheese
from .serializers import MilkSerializer, KefirSerializer, CheeseSerializer, CabbCheeseSerializer

# Create your views here.

# the views below represent collection/object api-endpoints
# and can be simplified sooner

#######Milk API
class MilkViewSet(viewsets.ModelViewSet):
	queryset = Milk.objects.all()
	serializer_class = MilkSerializer

#######

#######Kefir API
class KefirViewSet(viewsets.ModelViewSet):
	queryset = Kefir.objects.all()
	serializer_class = KefirSerializer

#######

#######Cheese API
class CheeseViewSet(viewsets.ModelViewSet):
	queryset = Cheese.objects.all()
	serializer_class = CheeseSerializer

#######

#######CabbageCheese API
class CabbCheeseViewSet(viewsets.ModelViewSet):
	queryset = CabbageCheese.objects.all()
	serializer_class = CabbCheeseSerializer

#######