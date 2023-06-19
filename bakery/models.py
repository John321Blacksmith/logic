from django.db import models

# Create your models here.

class Bread(models.Model):
	"""
	This model represents
	every pastry product.
	"""
	name = models.CharField(max_length=30)
	bread_type = models.CharField(max_length=20)
	weight = models.IntegerField()
	date = models.DateField()
	vendor = models.CharField(max_length=40)

	def __str__(self):
		return self.name