"""
This script fetches the necessary conifgurations from the special file
and assembles an object for the database interaction.
"""

from configparser import ConfigParser


def config(filename, section='postgresql'):
	# create a parser
	parser = ConfigParser()

	# reading the config file
	parser.read(filename)

	# define the database parameters object
	db_params = {}

	# looking into the section
	if parser.has_section(section):
		params = parser.items(section)

		for param in params:
			db_params[param[0]] = param[1]

	else:
		raise Exception(f'Section {section} not found in file {filename}.')

	return db_params 