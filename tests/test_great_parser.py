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
		# define an example issue
		self.improper_string = 'he3\nl4l  /^#;,\to/]w!o;r{l5d'

		# define the results suppossed to be
		self.decimal_number = 34.5
		self.sentence = 'hello world'

		# get a .json confs file
		self.m_confs = great_parser.decode_json_data('test_market_confs.json')

	def test_refine_string(self):
		"""Check if the refine_string method works well."""

		# trying to get a proper number that'll satisfy the example above
		proper_num = great_parser.DataFetcher.refine_string('food', self.improper_string, self.m_confs, numbers_only=True)
		
		# trying to get a proper sentence that'll satisfy the example above
		proper_sentence = great_parser.DataFetcher.refine_string('food', self.improper_string, self.m_confs, lang='en')

		# checking if anything is all right with the number
		self.assertEqual(self.decimal_number, proper_num)
		
		# checking if anything is all right with the number
		self.assertEqual(self.sentence, proper_sentence)

	def test_fetch_content(self):
		"""This method tests the work of the fetch_content method."""
		pass

	def test_structure_data(self):
		"""This method tests the work of the structure_data method."""
		pass


if __name__ == '__main__':
	unittest.main()