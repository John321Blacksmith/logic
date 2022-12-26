import sys
from . import secrs
from django.shortcuts import render

sys.path.append(secrs.project_location)

from logic_side.data_manager.config import config
from logic_side.data_manager import database_manager
from logic_side.scraping_tools.great_parser import DataFetcher
from api import ali_express

# Create your views here.

def retrieve_data_from_the_current_db(database_name):
	"""This function does fetch data from different
	   databases via performing the same commands. It 
	   then returns a context to be rendered on the html page."""

	# a selection query command
	selection_query = """SELECT {0}, {1}, {2}, {3} FROM {4};"""

	# create a connection object
	connection = database_manager.connect_to_the_db(secrs.params_location)

	# then extract the objects from a particular database
	objects = database_manager.retrieve_data(connection, selection_query, database_name)

	# form and return a context
	context = {
		'products': objects
	}

	return context


def index(request):
	"""This function renders a main page of the market."""

	# this page contains the top-most goods classified to the categories
	# there are the categories of either food and the other products at sidebars,
	# and there are the newest or price-offed highlighted products gathered from different
	# markets(sites) in the main site square.

	context = retrieve_data_from_the_current_db('highlights')

	return render(request, 'market/index.html', context)


def get_food(request):
	context = retrieve_data_from_the_current_db('food')
	return render(request, 'market/food.html', context)


def get_kitchen(request):
	context = retrieve_data_from_the_current_db('kitchen')
	return render(request, 'market/kitchen.html', context)


def get_electrical_equipment(request):
	context = retrieve_data_from_the_current_db('electr_equipment')
	return render(request, 'market/electr_eqnt.html', context)


def get_garden(request):
	context = retrieve_data_from_the_current_db('home_garden')
	return render(request, 'market/get_garden.html', context)


def get_kids_stuff(request):
	context = retrieve_data_from_the_current_db('for_kids')
	return render(request, 'market/kids_stuff.html', context)


def get_tools(request):
	context = retrieve_data_from_the_current_db('tools')
	return render(request, 'market/tools.html', context)


def get_fitness_stuff(request):
	context = retrieve_data_from_the_current_db('for_fitness')
	return render(request, 'market/fitness_stuff.html', context)


def get_auto_and_moto(request):
	context = retrieve_data_from_the_current_db('auto_moto')
	return render(request, 'market/auto_moto.html', context)


def get_beaut_and_health(request):
	context = retrieve_data_from_the_current_db('beauty_health')
	return render(request, 'market/beauty_health.html', context)