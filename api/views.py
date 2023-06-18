from rest_framework import generics
from diary.models import Milk, Kefir, Cheese, CabbageCheese
from .serializers import MilkSerializer, KefirSerializer, CheeseSerializer, CabbCheeseSerializer

# Create your views here.

# the views below represent collection/object api-endpoints
# and can be simplified sooner

#######Milk API
class MilkList(generics.ListCreateAPIView):
	queryset = Milk.objects.all()
	serializer_class = MilkSerializer


class MilkDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Milk.objects.all()
	serializer_class = MilkSerializer

#######

#######Kefir API
class KefirList(generics.ListCreateAPIView):
	queryset = Kefir.objects.all()
	serializer_class = KefirSerializer


class KefirDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Kefir.objects.all()
	serializer_class = KefirSerializer
#######

#######Cheese API
class CheeseList(generics.ListCreateAPIView):
	queryset = Cheese.objects.all()
	serializer_class = CheeseSerializer


class CheeseDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Cheese.objects.all()
	serializer_class = CheeseSerializer
#######

#######CabbageCheese API
class CabbCheeseList(generics.ListCreateAPIView):
	queryset = CabbageCheese.objects.all()
	serializer_class = CabbCheeseSerializer


class CabbCheeseDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = CabbageCheese.objects.all()
	serializer_class = CabbCheeseSerializer
#######