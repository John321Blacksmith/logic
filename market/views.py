import sys
from django.shortcuts import render, redirect
from . import secrs

sys.path.append(secrs.project_location)

from logic_side.credentials.config import config
from logic_side.scraping_tools import great_parser


ali_express_confs = great_parser.decode_json_data('market//ali_express_market.json')

# Create your views here.


def get_just_scraped_data(category):
	"""
	This function does extraction of the actual web data from the webpage.
	It then returns a template context.
	"""

	web_p_content = great_parser.DataFetcher.fetch_content(ali_express_confs[category]['source'], category, ali_express_confs)
	objects = great_parser.DataFetcher.structure_data(category, ali_express_confs, web_p_content)

	context = {
		'products': objects
	}

	return context


def index(request):
	"""
	This function renders a main page of the market.
	"""
	context = get_just_scraped_data('highlights')
	return render(request, 'market/index.html', context)


def get_food(request):
	context = get_just_scraped_data('food')
	return render(request, 'market/food.html', context)


def get_kitchen(request):
	context = get_just_scraped_data('kitchen')
	return render(request, 'market/kitchen.html', context)


def get_electrical_equipment(request):
	context = get_just_scraped_data('electr_equipment')
	return render(request, 'market/electr_eqnt.html', context)


def get_garden(request):
	context = get_just_scraped_data('home_garden')
	return render(request, 'market/get_garden.html', context)


def get_kids_stuff(request):
	context = get_just_scraped_data('for_kids')
	return render(request, 'market/kids_stuff.html', context)


def get_tools(request):
	context = get_just_scraped_data('tools')
	return render(request, 'market/tools.html', context)

def get_office(request):
	context = get_just_scraped_data('computer_office')
	return render(request, 'market/office.html', context)


def get_fitness_stuff(request):
	context = get_just_scraped_data('for_fitness')
	return render(request, 'market/fitness_stuff.html', context)


def get_auto_and_moto(request):
	context = get_just_scraped_data('auto_moto')
	return render(request, 'market/auto_moto.html', context)


def get_beauty_and_health(request):
	context = get_just_scraped_data('beauty_health')
	return render(request, 'market/beauty_health.html', context)