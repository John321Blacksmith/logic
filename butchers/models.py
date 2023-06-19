from django.db import models

# Create your models here.


class Meat(models.Model):
	"""
	This model represents the
	meat product.
	"""
	weight = models.IntegerField()
	meat_type = models.CharField(max_length=25)
	is_raw = models.BooleanField()
	date = models.DateField()
	supplier = models.CharField(max_length=40)

	def __str__(self):
		return self.meat_type
