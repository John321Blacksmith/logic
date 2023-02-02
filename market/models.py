from django.db import models

# Create your models here.


class Food(models.Model):
	product_name = models.CharField(max_length=255)
	product_price = models.DecimalField(max_digits=6, decimal_places=2)
	product_link = models.URLField(max_length=255)
	product_image = models.URLField(max_length=255)

	def __str__(self):
		if len(self.product_name) >= 50:
			return f'{self.product_name[:47]}...'


class BeautyHealth(models.Model):
	product_name = models.CharField(max_length=255)
	product_price = models.DecimalField(max_digits=6, decimal_places=2)
	product_link = models.URLField(max_length=255)
	product_image = models.URLField(max_length=255)

	def __str__(self):
		if len(self.product_name) >= 50:
			return f'{self.product_name[:47]}...'


class ElectricalEquipment(models.Model):
	product_name = models.CharField(max_length=255)
	product_price = models.DecimalField(max_digits=6, decimal_places=2)
	product_link = models.URLField(max_length=255)
	product_image = models.URLField(max_length=255)

	def __str__(self):
		if len(self.product_name) >= 50:
			return f'{self.product_name[:47]}...'


class AutoMoto(models.Model):
	product_name = models.CharField(max_length=255)
	product_price = models.DecimalField(max_digits=6, decimal_places=2)
	product_link = models.URLField(max_length=255)
	product_image = models.URLField(max_length=255)

	def __str__(self):
		if len(self.product_name) >= 50:
			return f'{self.product_name[:47]}...'


class ForKids(models.Model):
	product_name = models.CharField(max_length=255)
	product_price = models.DecimalField(max_digits=6, decimal_places=2)
	product_link = models.URLField(max_length=255)
	product_image = models.URLField(max_length=255)

	def __str__(self):
		if len(self.product_name) >= 50:
			return f'{self.product_name[:47]}...'


class ForFitness(models.Model):
	product_name = models.CharField(max_length=255)
	product_price = models.DecimalField(max_digits=6, decimal_places=2)
	product_link = models.URLField(max_length=255)
	product_image = models.URLField(max_length=255)

	def __str__(self):
		if len(self.product_name) >= 50:
			return f'{self.product_name[:47]}...'


class HomeGarden(models.Model):
	product_name = models.CharField(max_length=255)
	product_price = models.DecimalField(max_digits=6, decimal_places=2)
	product_link = models.URLField(max_length=255)
	product_image = models.URLField(max_length=255)

	def __str__(self):
		if len(self.product_name) >= 50:
			return f'{self.product_name[:47]}...'


class ComputerOffice(models.Model):
	product_name = models.CharField(max_length=255)
	product_price = models.DecimalField(max_digits=6, decimal_places=2)
	product_link = models.URLField(max_length=255)
	product_image = models.URLField(max_length=255)

	def __str__(self):
		if len(self.product_name) >= 50:
			return f'{self.product_name[:47]}...'


class Highlights(models.Model):
	product_name = models.CharField(max_length=255)
	product_price = models.DecimalField(max_digits=6, decimal_places=2)
	product_link = models.URLField(max_length=255)
	product_image = models.URLField(max_length=255)

	def __str__(self):
		if len(self.product_name) >= 50:
			return f'{self.product_name[:47]}...'
