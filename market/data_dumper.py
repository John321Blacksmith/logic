"""
This module contains functonality to dump data to every database table.
"""
import sys
from . import secrs
sys.path.append(secrs.project_location)
from logic_side.scraping_tools import great_parser


def dump_data(market_confs: dict):
	"""This function does update of the existing tables of the database."""
	# importing models here
	pass
