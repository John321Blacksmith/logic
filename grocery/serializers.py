from rest_framework import serializers
from .models import Vegetable, Fruit


class VegetableSerializer(serializers.ModelSerializer):
	class Meta:
		model = Vegetable
		fields = ('name', 'weight', 'date', 'supplier',)


class FruitSerializer(serializers.ModelSerializer):
	class Meta:
		model = Fruit
		fields = ('name', 'weight', 'date', 'supplier',)