from django.db import models

# Create your models here.


class AbsMenu(models.Model):
	"""
	This module is an abstract gives the main properties to the ones below.
	"""
	existence = models.BooleanField(default=True, verbose_name='visiblity')
	order = models.IntegerField(default=True, verbose_name='order')

	class Meta:
		abstract = True

	def __str__(self):
		return self.order


class Menu(AbsMenu):
	"""
	The main layer of the menu block.
	"""
	title = models.CharField(max_length=50, verbose_name='title')
	slug = models.SlugField(max_length=255, verbose_name='slug')
	named_url = models.CharField(max_length=255, blank=True, verbose_name='named_url')
	url = models.CharField(max_length=255, verbose_name='url')

	class Meta:
		verbose_name = 'menu name'
		verbose_name_plural = 'menu names'


	def __str__(self):
		return self.title


class MenuEntity(AbsMenu):
	"""
	The second layer of the menu block.
	"""
	menu = models.ForeignKey(Menu, on_delete=models.CASCADE, verbose_name='menu', blank=True, null=True)
	title = models.CharField(max_length=50, verbose_name='title')
	named_url = models.CharField(max_length=255, verbose_name='named_url', blank=True)

	class Meta:
		verbose_name = 'menu entity'
		verbose_name_plural = 'menu entities'

	def __str__(self):
		return self.title


class SubMenuEntity(AbsMenu):
	"""
	The third layer of the menu block.
	"""
	menu_entity = models.ForeignKey(MenuEntity, on_delete=models.CASCADE)
	title = models.CharField(max_length=50, verbose_name='title')
	named_url = models.CharField(max_length=255, verbose_name='named_url', blank=True)

	class Meta:
		verbose_name = 'sub-menu entity'
		verbose_name_plural = 'sub-menu entities'

	def __str__(self):
		return self.title
	