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
		self.decimal_number = '64,7432'
		self.even_number = '64'
		self.inconsistent_sentence = 'hello \nworld'
		self.confs = great_parser.decode_json_data('test_market_confs.json')
		self.soup = great_parser.DataFetcher.get_soup('markdown.txt', loc_file=True)

	def test_refine_string(self):
		"""Check if the refine_string method works well."""
		decimal_output = great_parser.DataFetcher.refine_string('food', self.decimal_number, self.confs, numbers_only=True)
		literal_output = great_parser.DataFetcher.refine_string('food', self.inconsistent_sentence, self.confs)
		
		self.assertEqual(decimal_output, '64.7432')
		self.assertEqual(literal_output, 'hello world')

	def test_fetch_content(self):
		"""This method tests the work of the fetch_content method."""
		pass

	def test_structure_data(self):
		"""This method tests the work of the structure_data method."""
		pass


if __name__ == '__main__':
	unittest.main()