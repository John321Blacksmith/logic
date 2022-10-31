import requests 
from bs4 import BeautifulSoup as Bs


class Soup(Bs):
	def __init__(self):
		super().__init__()
		
	@staticmethod
	def get_soup(source):
		page = requests.get(source, headers={'User-agent': 'Generic user agent'}).text
		soup = Bs(page, 'html.parser')
		
		return soup
		

class SortData:
	def __init__(self, seq):
		self.seq = seq
		
	def find_smallest(self):
		lowest = self.seq[0]
		lowest_id = 0
		
		for i in range(0, len(self.seq)):
			if self.seq[i] <= lowest:
				lowest = self.seq[i]
		else:
			return lowest
			
	def find_greatest(self):
		greatest = self.seq[0]
		greatest_id = 0
		
		for i in range(0, len(self.seq)):
			if self.seq[i] >= greatest:
				greatest = self.seq[i]
		else:
			return greatest


# data scraping from the target page
class DataFetcher(Soup):
	def __init__(self):
		super().__init__()

	@staticmethod
	def get_each_page(source, item, site_dict: dict):
		"""A method gets from the categories' page a link from each
		category on order to perform then the same operation
		as I have done before recursively."""

		soup = Soup.get_soup(source)

		all_vendors = soup.find_all(site_dict[item]['cats_links']['tag'], site_dict[item]['cats_links']['class'])
		vendors_links = []

		for i in all_vendors:
			link = site_dict[item]['source'][:21] + i['href']
			vendors_links.append(link)

		else:
			return vendors_links

	@staticmethod
	def refine_string(string: str):
		"""this method filters the string from the excessive space."""
		new_string = ''
		for letter in list(string):
			if (letter.isdigit()) or (letter != '') or (letter != ' ') or (letter != '\n'):
				new_string += letter

		return new_string
	
	@staticmethod
	def inspect_slashes(seq: str):
		"""this function iterates through the string
			 and finds the third forward slash inside one and
			 returns its index."""
		count = 0
		for i in range(0, len(seq)):
			if seq[i] == '/':
				count += 1
				if count == 3:
					return i
				else:
					continue

	@staticmethod
	def fetch_content(source, item, site_dict: dict):
		"""this method extracts the web data and allocates the four columns to the four lists."""
		content = {
			'titles': [],
			'integers': [],
			'links': [],
			'images': []
		}
		objects = Soup.get_soup(source).find_all(site_dict[item]['object']['tag'], site_dict[item]['object']['class'])
		
		for obj in objects:
			# derive a title
			if 'titles' in site_dict[item]['obj_components']:
				if 'class' not in site_dict[item]['title'].keys():
					title = obj.find(site_dict[item]['title']['tag']).text
				else:
					title = obj.find(site_dict[item]['title']['tag'], site_dict[item]['title']['class'])
					if title != None:
						content['titles'].append(title.text)
					
			# derive some integers
			if 'integers' in site_dict[item]['obj_components']:
				numbers = obj.find(site_dict[item]['integer']['tag'], site_dict[item]['integer']['class'])
				if numbers != None:	
					content['integers'].append(numbers.text)
				
			# derive a link
			if 'links' in site_dict[item]['obj_components']:
				
				link_element = obj.find(site_dict[item]['link']['tag'], site_dict[item]['link']['class'])
				
				if link_element == None:
					snippet = obj['href']
				else:
					snippet = link_element['href']
				
				if snippet.startswith('https://'):
					link = snippet
				else:
					third_slash = DataFetcher.inspect_slashes(site_dict[item]['source'])
					link = source[:third_slash] + '/' + snippet[1:]
					
				content['links'].append(link)
				
			# derive all the images in the product model
			if 'images' in site_dict[item]['obj_components']:
				images_house = obj.find_all(site_dict[item]['image']['tag'])
				for i in images_house:
					attrs = i.attrs
	
					for attr in attrs.keys():
						if attr == site_dict[item]['image']['attribute']:
							if i[attr].startswith('https://'):
								content['images'].append(i[attr])

		return content
		
	@staticmethod
	def structure_data(item, site_dict: dict, content_dict: dict):
		"""this method gathers the data from the lists above and 
		structures it so it is savable to the database."""
		list_of_objects = []
		quantities = []
		keys = [key for key in content_dict.keys()]
		
		for i in range(0, len(keys)):
			num = len(content_dict[keys[i]])
			if num != 0:
				quantities.append(num)
		
		ob = SortData(quantities)
		actual_num = ob.find_smallest()

		for i in range(0, actual_num):
			obj = {}
			
			if 'titles' in site_dict[item]['obj_components']:
				title = content_dict['titles'][i]
				obj['title'] = title.strip()
				
			if 'integers' in site_dict[item]['obj_components']:
				integer = content_dict['integers'][i]
				obj['integer'] = integer.strip()
				
			if 'links' in site_dict[item]['obj_components']:
				link = content_dict['links'][i]
				obj['link'] = link
				
			if 'images' in site_dict[item]['obj_components']:
				image = content_dict['images'][i]
				obj['image'] = image
		
			list_of_objects.append(obj)
			
		return list_of_objects