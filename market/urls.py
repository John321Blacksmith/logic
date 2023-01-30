from django.urls import path
from . import views

app_name = 'market'
# url patterns of the app here 

urlpatterns = [
	# index page pattern
	path('', views.index, name='index'),
	# the food page pattern
	path('food/', views.get_food, name='food'),
	# the kitchen page pattern
	path('kitchen/', views.get_kitchen, name='kitchen'),
	# the electrical equipment page pattern
	path('electr-equipment/', views.get_electrical_equipment, name='el_equip'),
	# the garden page pattern
	path('garden/', views.get_garden, name='garden'),
	# the kids stuff page pattern
	path('for-kids/', views.get_kids_stuff, name='kids_stuff'),
	# the tools page pattern
	path('tools/', views.get_tools, name='tools'),
	# the office page pattern
	path('tools/', views.get_office, name='office'),
	# the fitness page pattern
	path('fitness/', views.get_fitness_stuff, name='fitness_stuff'),
	# the auto and moto page pattern
	path('auto-moto/', views.get_auto_and_moto, name='auto_moto'),
	# the beauty and health page pattern
	path('beauty-health/', views.get_beauty_and_health, name='beauty_health'),

]