"""
This manager contains the functionality
covers the main database operations.
"""

import psycopg2
from .config import config

ERROR = 'operation failed because: '


def connect_to_the_db(filename):
	"""This function returns a connection object."""
	connection = None

	try:
		# get the connection parameters
		params = config(filename=filename)

		# assign a connection object to the variable
		connection = psycopg2.connect(**params)

	except (Exception, psycopg2.DatabaseError) as error:
		print(ERROR + str(error))

	else:
		return connection


def insert_data(conn, query, objects):

	# create a cursor
	cursor = conn.cursor()

	try:
		# operate a query
		for obj in objects:

			# extract the native object keys
			keys = [key for key in obj.keys()]

			# create a tuple of object values to be dumped
			values = (obj[keys[0]], obj[keys[1]], obj[keys[2]], obj[keys[3]])

			cursor.execute(query, values)

		# shut down the cursor
		cursor.close()

		# fix all the changes
		conn.commit()

		print('The data hass been successfully loaded to the database.')

	except (Exception, psycopg2.DatabaseError) as error:
		print(ERROR + str(error))

	finally:
		if conn is not None:
			conn.close()


def retrieve_data(conn, query):

	# create a cursor
	cursor = conn.cursor()

	# pass
	pass




def create_table(conn, query, tables):

	try:
		# create a cursor
		cursor = conn.cursor()

		# operate a query
		for table in tables:
			cursor.execute(query.format(table))

		# close the cursor
		cursor.close()

		# commit the changes
		conn.commit()

		print('table has been successfully created.')
	except (Exception, psycopg2.DatabaseError) as error:
		print(ERROR + str(error))

	finally:
		if conn is not None:
			conn.close()


def delete_data():
	pass

