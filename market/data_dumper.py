"""
This module contains functonality to dump data to every database.
"""
import sys
from . import secrs
sys.path.append(secrs.project_location)
from logic_side.data_manager import database_manager
from logic_side.scraping_tools import great_parser


def dump_data(market_confs: dict):
	"""This function does update of the existing tables of the database."""
	tables = [key for key in market_confs.keys()]

	insertion_query = """INSERT INTO {0}(product_name, product_price, product_link, product_image)
						 VALUES('{1}','{2}','{3}','{4}');"""

	for table in tables[2:]:
		connection = database_manager.connect_to_the_db(secrs.params_location)
		content = great_parser.DataFecther.fetch_content(market_confs[table]['source'], table, market_confs)
		products = great_parser.DataFetcher.structure_data(table, market_confs, content)

		database_manager.insert_data(connection, table, insertion_query, products)
