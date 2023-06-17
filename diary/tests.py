from django.test import TestCase
from .models import Milk, Kefir, Cheese, CabbageCheese
# Create your tests here.


class TestDiaryModels(TestCase):

	@classmethod
	def setUpTestData(cls):
		cls.liquid_product = Milk.objects.create(
					title='test title',
					vendor='test vendor',
					price=999.99,
					image='https://static.test/999.jpeg',
					category='test category',
					fat=999.9,
					protein=999.9,
					calories=999,
					volume=999.9,
			)
		cls.hard_product = Cheese.objects.create(
					title='test title',
					vendor='test vendor',
					price=999.99,
					image='https://static.test/999.jpeg',
					category='test category',
					fat=999.9,
					protein=999.9,
					calories=999,
					weight=999,
			)

	def test_liquid_products_model_data(self):
		"""
		check if all the fields of
		every liquid product
		are saved properly.
		"""
		self.assertEqual(self.liquid_product.title, 'test title')
		self.assertEqual(self.liquid_product.vendor, 'test vendor')
		self.assertEqual(self.liquid_product.price, 999.99)
		self.assertEqual(self.liquid_product.image, 'https://static.test/999.jpeg')
		self.assertEqual(self.liquid_product.category, 'test category')
		self.assertEqual(self.liquid_product.fat, 999.9)
		self.assertEqual(self.liquid_product.protein, 999.9)
		self.assertEqual(self.liquid_product.calories, 999)
		self.assertEqual(self.liquid_product.volume, 999.9)

	def test_liquid_products_model_data(self):
		"""
		check if all the fields of
		every hard product
		are saved properly.
		"""
		self.assertEqual(self.hard_product.title, 'test title')
		self.assertEqual(self.hard_product.vendor, 'test vendor')
		self.assertEqual(self.hard_product.price, 999.99)
		self.assertEqual(self.hard_product.image, 'https://static.test/999.jpeg')
		self.assertEqual(self.hard_product.category, 'test category')
		self.assertEqual(self.hard_product.fat, 999.9)
		self.assertEqual(self.hard_product.protein, 999.9)
		self.assertEqual(self.hard_product.calories, 999)
		self.assertEqual(self.hard_product.weight, 999)
# PASSED