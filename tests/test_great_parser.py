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

	def test_refine_string(self):
		"""Check if the refine_string method works well."""
		decimal_output = great_parser.DataFetcher.refine_string('food', self.decimal_number, self.confs, numbers_only=True)
		literal_output = great_parser.DataFetcher.refine_string('food', self.inconsistent_sentence, self.confs)
		
		self.assertEqual(decimal_output, '64.7432')
		self.assertEqual(literal_output, 'hello world')


if __name__ == '__main__':
	unittest.main()