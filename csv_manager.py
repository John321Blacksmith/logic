# */scraping_tools/csv_manager.py

import csv
from openpyxl import Workbook
from great_parser import DataFetcher as Df
from api import klen_market, news_data


def write_to_the_csv_file(contents, writer_object):
	"""This function takes both a writer object and a list
	 of objects and does loading to the file."""
	 # create the first line for columns
	writer_object.writeheader()
	
	# pass over the list of objects		
	for i in range(0, len(contents)):
		# write each one to the file via the writer object's method
		writer_object.writerow(contents[i])
		


def load_entire_data(links, file_name, item, site_dict: dict):
	"""This function gets the web data and pushes it to the csv-file.
	It is oriented on the dictionary that is received as an argument."""
	# the keys to be used as names of the column
	fields = ['title', 'integer', 'link', 'image']
	
	# open or create a file
	with open(file_name, mode='a', encoding='utf-8') as f:
		# create a writer object which has the fieldnames
		csv_writer = csv.DictWriter(f, fieldnames=fields)
		
		# iterate through the links 
		for i in range(0, len(links)):
			# get all the unstructured content from the page
			products_content = Df.fetch_content(links[i], item, site_dict)
			# get a structured list of objects
			products = Df.structure_data(item, site_dict, products_content)
			
			# write to a csv file
			write_to_the_csv_file(products, csv_writer)
		else:
			print(f'The data has been successfully loaded to the file \'{file_name}\'. ')
			
			
def read_from_csv_file(file_name):
	"""This function picks up all the data from the csv-file 
	and either processes and renders it."""
	
	try:
		with open(file_name, mode='r', encoding='utf-8') as f:
			csv_reader = csv.reader(f, delimiter=',')
			line_count = 0
			
			for row in csv_reader:
				if line_count == 0:
					print(f'Column names are {", ".join(row)}')
					line_count += 1
				else:
					print(f'\tName: {row[0]}, Price: {row[1]}, Link: {row[2]}, Image: {row[3]}')
			else:
				print(f'{line_count} lines have been rendered.')
	
	except FileNotFoundError:
		print(f'The file \'{file_name}\' does not exist or is located in another directory.')


def write_to_excel(file_name, ws_title):
	wb = Workbook()
	ws = wb.active
	
	ws.title = ws_title
	
	col_names = ['Name', 'Price', 'Link', 'Image']
	
	with open(file_name, mode='r', encoding='utf-8') as f:
		csv_reader = csv.reader(f, delimiter=',')
		
		line_count = 0
		
		for row in csv_reader:
			if line_count == 0:
				ws.append(col_names)
				line_count += 1
			else:
				if [row[0], row[1], row[2], row[3]] != ['title', 'integer', 'link', 'image']:
					ws.append([row[0], row[1] + ' ₽', row[2], row[3]])
					line_count += 1
		else:
			excel_file = file_name[:-4] + '.xlsx'
			wb.save(excel_file)
	
	print(f'Created file \'{excel_file}\'.')
	


