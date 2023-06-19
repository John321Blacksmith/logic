from django.db import models

# Create your models here.

class Product(models.Model):
	"""
	This model describes a product
	that can be either Vegetable or
	Fruit.
	"""
	name = models.CharField(max_length=20)
	weight = models.IntegerField()
	date = models.DateField()
	supplier = models.CharField(max_length=40)

	class Meta:
		abstract = True

	def __str__(self):
		return self.title


class Vegetable(Product):
	"""
	This model represents all
	the vegetables.
	"""


class Fruit(Product):
	"""
	This model represents all
	the fruits.
	"""
