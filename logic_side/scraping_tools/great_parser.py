# */scraping_tools/great_parser.py

# This module contains either scraping and data structuring functionality.

import requests
from bs4 import BeautifulSoup as Bs


class Soup(Bs):
   """Create a soup object."""

   def __init__(self):
      super().__init__()

   @staticmethod
   def get_soup(source, loc_file=False):
      """Returning a soup."""

      my_headers = {
         'User-Agent':
         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15'
      }

      if loc_file:
         with open(source, mode='r', encoding='utf-8') as page:
            soup = Bs(page, 'html.parser')

      if not loc_file:
         page = requests.get(source, headers=my_headers).text
         soup = Bs(page, 'html.parser')

      return soup


class SortData:
   """The sorting algorithm finds either a lowest or a greatest value in the list."""

   def __init__(self, seq):
      self.seq = seq

   def find_smallest(self):
      """This method returns a lowest value."""
      lowest = self.seq[0]

      for i in range(0, len(self.seq)):
         if self.seq[i] <= lowest:
            lowest = self.seq[i]
      else:
         return lowest

   def find_greatest(self):
      """This method returns a greatest value."""
      greatest = self.seq[0]

      for i in range(0, len(self.seq)):
         if self.seq[i] >= greatest:
            greatest = self.seq[i]
      else:
         return greatest


# data scraping from the target page
class DataFetcher(Soup):
   """This class creates either an object contains unstructured web-page
     data and the one represents a structured list of objects."""

   def __init__(self):
      super().__init__()

   @staticmethod
   def get_each_page(source, item, site_dict: dict, loc_file=False):
      """A method gets from the categories' page a link from each
        category in order to perform then the same operation
        as I have done before recursively."""
        
      if loc_file:
      	soup = DataFetcher.get_soup(source, loc_file=True)
      if not loc_file:
      	soup = Soup.get_soup(source)

      all_categories = soup.find_all(site_dict[item]['cats_links']['tag'],
                                     site_dict[item]['cats_links']['class'])
      categories_links = []

      third_slash = DataFetcher.inspect_signs('/', source, 3)

      for category in all_categories:
         link = source[:third_slash] + '/' + category['href'][1:]
         categories_links.append(link)

      else:
         return categories_links
         
   @staticmethod
   def get_a_generic_pages_amount(source,
   								  item,
   								  site_dict: dict,
   								  loc_file=False):
    	"""This method finds out how many objects there are in the
    	 current category in total. Then it returns an actual number
    	 of pages to be in the category."""
    	
    	if loc_file:
    		soup = DataFetcher.get_soup(source, loc_file=True)
    	if not loc_file:
    		soup = DataFetcher.get_soup(source)
    		
    	list_of_objects = soup.find_all(site_dict[item]['object']['tag'],
    									site_dict[item]['object']['class'])
    									
    	objs_quantity_per_page = len(list_of_objects)
    	total_objs_quantity = DataFetcher.refine_string(soup.find(site_dict[item]['generic_quantity']['tag'],
    																  site_dict[item]['generic_quantity']['class']).text,
    																  numbers_only=True)
    	
    	total_number_of_pages = total_objs_quantity // objs_quantity_per_page
    	
    	return total_number_of_pages

   @staticmethod
   def refine_string(problematic_string: str, numbers_only=False):
      """this method filters the string from the excessive space.
      Returns digits or letters."""
      data = ''

      if numbers_only:
         for letter in list(problematic_string):
            if (letter.isdigit()) or (letter == ','):
                data += letter
         else:
            if data.find(','):
               decimal = data.replace(',', '.')
               if decimal == '':
                  result = 'no data'
               else:
                  result = float(decimal)
            else:
               result = int(data)
      else:
         for letter in list(problematic_string):
            if (letter != '\n') and (letter != '\t'):
                  data += letter
         else:
            result = data

      return result

   @staticmethod
   def inspect_signs(sign: str, seq: str, sign_num: int):
      """This method gets a sign to search and the row of data to
         be inspected and iterates then through the row
         and finds the issued sign inside one and
         returns its position."""
      count = 0
      for i in range(0, len(seq)):
         if seq[i] == sign:
            count += 1
            if count == sign_num:
               return i
            else:
               continue

   @staticmethod
   def fetch_content(source, item, site_dict: dict, loc_file=False):
      """This method creates an object represents a dictionary which
         contains four universal keys that have lists as their values.
         The dictionary keys: 'titles', 'integers', 'links', 'images'.
         Every key of this dictionary is related to all the data gathered from the
       page for the data the dict key represents."""

      # a dictionary with the web data to be further structured
      content = {'titles': [], 'integers': [], 'links': [], 'images': []}

      # find all the individual objects on the page and get a list of them
      if loc_file:
         soup = Soup.get_soup(source, loc_file=True)

      if not loc_file:
         soup = Soup.get_soup(source)

      objects = soup.find_all(site_dict[item]['object']['tag'],
                              site_dict[item]['object']['class'])

      # strolling through the derived list and extraction of each key data from every list object
      for obj in objects:
         # derive a title
         # if any object is in the list of componets every api item has, the extraction of HTML data will be performed
         if 'titles' in site_dict[item]['obj_components']:
            # if there is no a 'class' key in the 'title' object of the api item, a 'tag' key will be used only
            if 'class' not in site_dict[item]['title'].keys():
               if 'attribute' in site_dict[item]['title'].keys():
                  titles_house = obj.find_all(site_dict[item]['title']['tag'])
                  for t in titles_house:
                     t_attrs = t.attrs
                     for attr in t_attrs.keys():
                        if attr == site_dict[item]['title']['attribute']:
                           if t[attr] == site_dict[item]['title']['attr_value']:
                              title = t
               else:
                  title = obj.find(site_dict[item]['title']['tag'])

            else:
               title = obj.find(site_dict[item]['title']['tag'],
                                site_dict[item]['title']['class'])

            # here we have an entity of one of the four types of web page content
            if title != None:
               # if this entity is not None, it'll be sent to its family
               content['titles'].append(title.text)
            else:
            	content['titles'].append('empty')

         # derive some integers
         if 'integers' in site_dict[item]['obj_components']:
            numbers = obj.find(site_dict[item]['integer']['tag'],
                               site_dict[item]['integer']['class'])
            if numbers != None:
               content['integers'].append(numbers.text)

         # derive a link
         if 'links' in site_dict[item]['obj_components']:
            if 'class' in site_dict[item]['link'].keys():
               link_element = obj.find(site_dict[item]['link']['tag'],
                                       site_dict[item]['link']['class'])
            else:
               link_element = obj.find(site_dict[item]['link']['tag'])

            # if the link entity is None, the current list object itself will be used, assuming it has the 'href' attribute
            if link_element == None:
               snippet = obj['href']
            # if everything is fine, the href data will be extracted from one of the elements of the list object
            else:
               snippet = link_element['href']

            # check if the link entity is comprehensive or not
            # if so, nothing changes
            if snippet.startswith('https://'):
               link = snippet
            # if it is not, a root link is cut off from the main source of the item
            else:
               # fetching an end point of the sliced string
               third_slash = DataFetcher.inspect_signs('/', source, 3)
               # then the main source string slice, an additional slash and the uncomplete href are substracted
               link = source[:third_slash] + '/' + snippet[1:]
            
            content['links'].append(link)

         # derive all the images in the product model
         if 'images' in site_dict[item]['obj_components']:
            # here we find all the images inlined in the list object
            images_house = obj.find_all(site_dict[item]['image']['tag'])
            # iterate through these images to inspect then all the attributes of each one
            for i in images_house:
               attrs = i.attrs
               # go through the attributes of each image
               for attr in attrs.keys():
                  # check if the current attribute is equal to the one required in the item api
                  if attr == site_dict[item]['image']['attribute']:
                     # if so, the attribute is checked if it has a comprehensive link
                     if i[attr].startswith('https://'):
                        image_link = i[attr]
                     else:
                        if i[attr].startswith('//'):
                           first_slash = DataFetcher.inspect_signs('/',
                              source, 1)
                           image_link = source[:first_slash] + '/' + i[attr][1:]
                        else:
                           third_slash = DataFetcher.inspect_signs('/',
                              source, 3)
                           image_link = source[:third_slash] + '/' + i[attr][1:]

                     # append this entity to the images family
                     content['images'].append(image_link)

      # and eventually, the content dictionary is created and returned as a dict object
      return content

   @staticmethod
   def structure_data(item, site_dict: dict, content_dict: dict):
      """This method takes an item key string, an api dictionary
        and a content dictionary with unsctructured data, and it then
         returns a structured list with objects."""

      # a list of structured objects assembled along
      list_of_objects = []

      quantities = []
      keys = [key for key in content_dict.keys()]

      for i in range(0, len(keys)):
         # get an amount of each list
         num = len(content_dict[keys[i]])
         # check if the list is not empty
         if num != 0:
            quantities.append(num)

      # check if the list of amounts is not empty
      if len(quantities) != 0:
         # if so, this list is processed by the sorting algorithm
         ob = SortData(quantities)
         actual_num = ob.find_smallest()
         for i in range(0, actual_num):
            # every object is constructed as a dictionary
            obj = {}

            for key in keys:
               DataFetcher.check_components(i, item, key, site_dict, content_dict, obj)

            # when the object dict is constructed, it is moved to the list of objects
            list_of_objects.append(obj)

      return list_of_objects

   @staticmethod
   def check_components(order_num,
                        item,
                        item_key: str,
                        site_dict: dict,
                        content_dict: dict,
                        obj_dict: dict):
    # before every item of object is included to the object, there is a check
    # if a required key is in the item list of components

      if item_key in site_dict[item]['obj_components']:
         obj_entity = content_dict[item_key][order_num]
         if item_key == 'titles':
            obj_dict[item_key[:-1]] = DataFetcher.refine_string(obj_entity)
         if item_key == 'integers':
            obj_dict[item_key[:-1]] = DataFetcher.refine_string(obj_entity, numbers_only=True)
         else:
            obj_dict[item_key[:-1]] = obj_entity