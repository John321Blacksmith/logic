import sys
from . import secrs
from django.shortcuts import render

sys.path.append(secrs.project_location)

from logic_side.data_manager import database_manager

# Create your views here.


def index(request):
	"""This function renders a main page of the market."""

	 # a selection query command
	selection_query = """SELECT {0}, {1}, {2}, {3} FROM {4};"""

	# create a connection object
	connection = database_manager.connect_to_the_db(secrs.params_location)

	# get data from the storage
	objects = database_manager.retrieve_data(connection, selection_query, 'food')

	# create a context
	context = {'products': objects}

	return render(request, 'market/index.html', context)


def update_storage(request):
	pass