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


def insert_data(conn, query, objects, tables):

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

		print('The data has been successfully loaded to the database.')

	except (Exception, psycopg2.DatabaseError) as error:
		print(ERROR + str(error))

	finally:
		if conn is not None:
			conn.close()


def retrieve_data(conn, query, table):
	"""This function fetches the data from the table and
	returns a list of objectsto be rendered in the django template."""

	objs = []
	try:
		# create a cursor
		cursor = conn.cursor()

		
		# operate the query 
		cursor.execute(query.format('product_name', 'product_price', 'product_link', 'product_image', table))

		# get a number of rows to be iterated
		rows_amount = cursor.rowcount

		# pass through the rows and get the values 
		# from each and define an object
		for i in range(0, rows_amount):

			# extract a table record
			row = cursor.fetchone()

			# define an object (the product id is by default on the zero index)
			obj = {
				'title': row[0],
				'price': row[1],
				'link': row[2],
				'image': row[3]
			}

			# put the object to the list
			objs.append(obj)

		# shut down the cursor
		cursor.close()

	except (Exception, psycopg2.DatabaseError) as error:
		print(ERROR + str(error))

	finally:
		if conn is not None:
			conn.close()

	return objs

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


def update_data(conn, query, tables):
	"""this function updates the data in the table."""

	cursor = conn.cursor()

	for table in tables:
		pass

def delete_data():
	pass

