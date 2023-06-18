from rest_framework import serializers
from diary.models import Milk, Kefir, Cheese, CabbageCheese

# there are serializers below which do the same things
# and can be designed in the cleaner way; so they will be further.

class MilkSerializer(serializers.ModelSerializer):
	class Meta:
		model = Milk
		fields = ['title', 'vendor', 'price', 'image', 'category', 'fat', 'protein', 'calories', 'volume']


class KefirSerializer(serializers.ModelSerializer):
	class Meta:
		model = Kefir
		fields = ['title', 'vendor', 'price', 'image', 'category', 'fat', 'protein', 'calories', 'volume']


class CheeseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cheese
		fields = ['title', 'vendor', 'price', 'image', 'category', 'fat', 'protein', 'calories', 'weight']


class CabbCheeseSerializer(serializers.ModelSerializer):
	class Meta:
		model = CabbageCheese
		fields = ['title', 'vendor', 'price', 'image', 'category', 'fat', 'protein', 'calories', 'weight']
