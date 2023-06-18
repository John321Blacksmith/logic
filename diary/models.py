from django.db import models

# Create your models here.

class Product(models.Model):
	"""
	This base model represents
	every product with common
	fields.
	"""
	title = models.CharField(max_length=250, help_text='f.e Product')
	vendor = models.CharField(max_length=150, help_text='f.e. Product&Health')
	price = models.DecimalField(max_digits=6, decimal_places=2, help_text='f.e. 9999.99')
	image = models.URLField(max_length=200, help_text='f.e. \'http:/static.exampl.com/77577mhf.jpeg\'')
	category = models.CharField(max_length=30, help_text='f.e. cheese')
	fat = models.DecimalField(max_digits=4, decimal_places=1, help_text='f.e. 999.9')
	protein = models.DecimalField(max_digits=4, decimal_places=1, help_text='f.e. 999.9')
	calories = models.IntegerField(help_text='f.e. 999')

	class Meta:
		abstract = True

	def __str__(self):
		return self.title


class LiquidProduct(Product):
	"""
	This child model describes
	all the liquid diary products.
	"""
	volume = models.DecimalField(max_digits=5, decimal_places=1, help_text='f.e 9999.9')

	class Meta:
		abstract = True


class HardProduct(Product):
	"""
	This child model describes
	all the hard diary products.
	"""
	weight = models.IntegerField(help_text='f.e 999')

	class Meta:
		abstract = True


# the models below has to be applied to the database table

class Milk(LiquidProduct):
	"""
	This grandchild model
	describes all the milk
	products.
	"""


class Kefir(LiquidProduct):
	"""
	This grandchild model
	describes all the kefir
	products.
	"""


class Cheese(HardProduct):
	"""
	This grandchild model
	describes all the cheeze
	products.
	"""


class CabbageCheese(HardProduct):
	"""
	This grandchild model
	describes all the cabage
	cheese products.
	"""