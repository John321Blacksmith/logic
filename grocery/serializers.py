from rest_framework import serializers
from .models import Vegetable, Fruit


class VegetableSerializer(serializers.ModelSerializer):
	class Meta:
		model = Vegetable
		fields = ('weight', 'date', 'supplier',)


class FruitSerializer(serializers.ModelSerializer):
	class Meta:
		model = Fruit
		fields = ('weight', 'date', 'supplier',)