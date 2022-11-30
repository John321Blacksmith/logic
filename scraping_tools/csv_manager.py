# */scraping_tools/csv_manager.py

import csv
from openpyxl import Workbook, load_workbook
from .great_parser import DataFetcher as Df


class FileManager(Df, Workbook):
	def __init__(self): 
		super().__init__()

	def write_to_the_text_file(self, file_name, content):
		if file_name:
			try:
				with open(file_name, mode='a', encoding='utf-8') as f:
					f.write(content)
			except FileNotFounderror:
				print(f'The file \'{file_name}\' not found.')

	def write_to_the_json_file(self, file_name, content):
		pass


	def write_to_the_csv_file(self,
								file_name,
								source,
								item,
								site_dict: dict,
								lang='en'):

		fields = ['title', 'integer', 'link', 'image']

		if lang == 'ru':
			fields = ['Наименование', 'Цена', 'Ссылка', 'Изображение']

		# open or create a csv file and create a writer object

		with open(file_name, mode='a', encoding='utf-8') as f:
			writer_object = csv.DictWriter(f, fieldnames=fields)

			content = Df.fetch_content(source, item, site_dict)
			objects = Df.structure_data(item, site_dict, content)

			writer_object.writeheader()

			for i in range(0, len(objects)):
				writer_object.writerow(objects[i])
			else:
				print(f'The data has been successfully loaded to the file \'{file_name}\'.')


	def write_to_the_excel_file(self, csv_file_name, cols_names):

		wb = load_workbook(filename=csv_file_name)

		# activate a workbook 
		work_sheet = wb.active

		# define a worksheet name
		# ws.title = ws_title

		with open(csv_file_name, mode='r') as f:
			csv_reader = csv.reader(f, delimiter=',')

			line_count = 0
			for row in csv_reader:
				if line_count == 0:
					work_sheet.append(cols_names)
					line_count += 1
				else:
					if [row[0], row[1], row[2], row[3]] != ['title', 'integer', 'link', 'image']:
						work_sheet.append(row[0], row[1] + ' rub', row[2], row[3])
						line_count += 1
			else:
				excel_file = csv_file_name[:-4] + '.xlsx'
				wb.save(excel_file)

		print(f'Created file \'{excel_file}\'.')