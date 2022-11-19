import re
from scraping_tools.great_parser import DataFetcher as Df
from api import klen_market


entity = input('What entity do you want to find?: ')

def search_engine(request, site_dict: dict):
	items = [key for key in site_dict.keys()]
	
	for item in items:
		links = Df.get_each_page(site_dict[item]['source'], item, site_dict)
		
		for i in range(0, len(links)):
			soup = Df.get_soup(links[i])
			html = soup.text
			
			if re.search(request, html, re.IGNORECASE):
				content = Df.fetch_content(links[i], item, site_dict)
				objs = Df.structure_data(item, site_dict, content)
				
				if len(objs) != 0:
					for j in range(0, len(objs)):
						if re.search(request, objs[j]['title'], re.IGNORECASE):
							print(objs[j])
				else:
					print('there is no content at all.')
						
			else:
				print(f'No matches on the \'{links[i]}\'')
				
		
if __name__ == '__main__':
	search_engine(entity, klen_market)
