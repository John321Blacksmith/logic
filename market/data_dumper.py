"""
This module contains functonality to dump data to every database table.
The program fetches the data from the web and sends it to the database via imported django models.
"""

import os
import sys
from django import setup
import secrs
sys.path.append(secrs.project_location)
from online_market import settings

# define the settings applied for this program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings.__name__)
setup()

from logic_side.scraping_tools import great_parser
from models import (
				Food,
				BeautyHealth,
				ElectricalEquipment,
				AutoMoto,
				ForKids,
				ForFitness,
				HomeGarden,
				ComputerOffice
				)



# get a market dictionary
m_dictionary = great_parser.decode_json_data('ali_express_market.json')

# create a hash table with models associations
market_tables = {
	'food': Food,
	'beauty_health': BeautyHealth,
	'electr_equipment': ElectricalEquipment,
	'auto_moto': AutoMoto,
	'for_kids': ForKids,
	'for_fitness': ForFitness,
	'home_garden': HomeGarden,
	'computer_office': ComputerOffice
	}


def dump_data(table_associations: dict, market_confs: dict):
	"""This function does update of the existing tables of the database."""
	
	# get all the table names
	tables = [table for table in table_associations.keys()]

	# first of all, iterate through the database models(tables)
	# in order to have a deal with each of them
	for table in tables:
		# involve the parser to get specific data for each table
		# for this, I utilize keys of hash table that should be similar to ones in the market dictionary
		content = great_parser.DataFetcher.fetch_content(market_confs[table]['source'], table, market_confs)

		# structure the web content
		objects = great_parser.DataFetcher.structure_data(table, market_confs, content)

		# iterate through all the objects and make database records
		for obj in objects:

			# define values
			product_name = obj['title']
			product_price = obj['integer']
			product_link = obj['link']
			product_image = obj['image']

			# instantiate a current table
			# and assign each table object's instance to the fetched value
			table_object = table_associations[table](product_name=product_name, product_price=product_price, product_link=product_link, product_image=product_image)

			# eventually, commit changes
			table_object.save()
		else:
			# track results by just printing
			print(f'The data has been loaded to the table \'{table}\'.')
	

if __name__ == '__main__':
	dump_data(market_tables, m_dictionary)