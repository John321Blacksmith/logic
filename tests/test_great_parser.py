import sys
import unittest
import secrs
sys.path.append(secrs.project_location)

# importing the modules to be tested
from logic_side.scraping_tools import great_parser


# do testing here
class TestGreatParser(unittest.TestCase):
	"""This test case covers all functionality of the great_parser.py."""

	def setUp(self):
		"""Define some constants."""
		pass

	def test_refine_string(self):
		"""Check if the refine_string method works well."""
		pass