# */scraping_tools/great_parser.py

# This module contains either scraping and data structuring functionality.
 
import requests 
from bs4 import BeautifulSoup as Bs


class Soup(Bs):
    """This class creates a soup object for a wide range of use."""

    def __init__(self):
        """A constructor of the object."""
        super().__init__()

    @staticmethod
    def get_soup(source):
        """This method takes a source of the page and returns a soup of it."""

        page = requests.get(source, headers={'User-agent': 'Generic user agent'}).text
        soup = Bs(page, 'html.parser')

        return soup


class SortData:
    """The sorting algorithm finds either a lowest or a greatest value in the list."""
    def __init__(self, seq):
        self.seq = seq

    def find_smallest(self):
        """This method returns a lowest value."""
        lowest = self.seq[0]
        lowest_id = 0

        for i in range(0, len(self.seq)):
            if self.seq[i] <= lowest:
                lowest = self.seq[i]
        else:
            return lowest

    def find_greatest(self):
        """This method returns a greatest value."""
        greatest = self.seq[0]
        greatest_id = 0

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
    def get_each_page(source, item, site_dict: dict):
        """A method gets from the categories' page a link from each
        category in order to perform then the same operation
        as I have done before recursively."""

        soup = Soup.get_soup(source)

        all_categories = soup.find_all(site_dict[item]['cats_links']['tag'], site_dict[item]['cats_links']['class'])
        categories_links = []

        third_slash = DataFetcher.inspect_slashes(source, 3)

        for category in all_categories:
            link = source[:third_slash] + '/' + category['href'][1:]
            categories_links.append(link)

        else:
            return categories_links

    @staticmethod
    def refine_string(string: str):
        """this method filters the string from the excessive space."""
        new_string = ''
        for letter in list(string):
            if (letter.isdigit()) or (letter != '') or (letter != ' ') or (letter != '\n'):
                new_string += letter

        return new_string

    @staticmethod
    def inspect_slashes(seq: str, slash_num: int):
        """this method iterates through the string
             and finds the third forward slash inside one and
             returns its position."""
        count = 0
        for i in range(0, len(seq)):
            if seq[i] == '/':
                count += 1
                if count == slash_num:
                    return i
                else:
                    continue

    @staticmethod
    def fetch_content(source, item, site_dict: dict):
        """This method creates an object represents a dictionary which
         contains four universal keys that have lists as their values.
         The dictionary keys: 'titles', 'integers', 'links', 'images'.
         Every key of this dictionary is related to all the data gathered from the
       page for the data the dict key represents."""

      # a dictionary with the web data to be further structured
        content = {
            'titles': [],
            'integers': [],
            'links': [],
            'images': []
        }

        # find all the individual objects on the page and get a list of them
        objects = Soup.get_soup(source).find_all(site_dict[item]['object']['tag'], site_dict[item]['object']['class'])

        # strolling through the derived list and extraction of each key data from every list object
        for obj in objects:
            # derive a title
            # if any object is in the list of componets every api item has, the extraction of HTML data will be performed
            if 'titles' in site_dict[item]['obj_components']:
                # if there is no a 'class' key in the 'title' object of the api item, a 'tag' key will be used only
                if 'class' not in site_dict[item]['title'].keys():
                    title = obj.find(site_dict[item]['title']['tag'])
                else:
                    title = obj.find(site_dict[item]['title']['tag'], site_dict[item]['title']['class'])

                # here we have an entity of one of the four types of web page content
                if title != None:
                    # if this entity is not None, it'll be sent to its family
                    content['titles'].append(title.text)

            # derive some integers
            # -|-|-|-|-|-
            if 'integers' in site_dict[item]['obj_components']:
                numbers = obj.find(site_dict[item]['integer']['tag'], site_dict[item]['integer']['class'])
                if numbers != None:
                    # -|-|-|-|-|-
                    content['integers'].append(numbers.text)

            # derive a link
            # -|-|-|-|-|-
            if 'links' in site_dict[item]['obj_components']:
                # -|-|-|-|-|-
                if 'class' in site_dict[item]['link'].keys():
                    link_element = obj.find(site_dict[item]['link']['tag'], site_dict[item]['link']['class'])
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
                    third_slash = DataFetcher.inspect_slashes(site_dict[item]['source'], 3)
                    # then the main source string slice, an additional slash and the uncomplete href are substracted
                    link = source[:third_slash] + '/' + snippet[1:]
                # -|-|-|-|-|-
                content['links'].append(link)

            # derive all the images in the product model
            # -|-|-|-|-|-
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
                                # -|-|-|-|-|-
                                image_link = i[attr]
                            else:
                                if i[attr].startswith('//'):
                                    first_slash = DataFetcher.inspect_slashes(site_dict[item]['source'], 1)
                                    image_link = site_dict[item]['source'][:first_slash] + '/' + i[attr][1:]
                                else:
                                    third_slash = DataFetcher.inspect_slashes(site_dict[item]['source'], 3)
                                    image_link = site_dict[item]['source'][:third_slash] + '/' + i[attr][1:]


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

        # derive all the keys from the content dictionary
        # in order to use each one as a key from each
        # list in the content dictionary and find an
        # amount of every list respectively.

        keys = [key for key in content_dict.keys()]

        for i in range(0, len(keys)):
            # get an amount of each list
            num = len(content_dict[keys[i]])
            # check if the list is not empty
            if num != 0:
                # if so, the number of list items is appended to the list above
                quantities.append(num)

        # check if the list of amounts is not empty
        if len(quantities) != 0:
            # if so, this list is processed by the sorting algorithm
            ob = SortData(quantities)
            # In order to structure all the elements from
            # different lists rationally and create objects,
            # a smallest value of the list of amounts is got so
            # as not to let some lists be greater of amount, for
            # all the four lists must be of the same length.
            actual_num = ob.find_smallest()

            # then we use a stead number got from the list and
            # go along that number. The number of objetcs must
            # be as well as the actual number itself represents
            for i in range(0, actual_num):
                # every object is constructed as a dictionary
                obj = {}

                # before every item of object is included to the object, there is a check
                # if a required key is in the item list of components
                for key in keys:
                    DataFetcher.check_components(i, item, key, site_dict, content_dict, obj)

                # when the object dict is constructed, it is moved to the list of objects
                list_of_objects.append(obj)

        # eventually, the list of all the web objects is returned
        return list_of_objects

    @staticmethod
    def check_components(order_num, item, item_key: str, site_dict: dict, content_dict: dict, obj_dict: dict):

        if item_key in site_dict[item]['obj_components']:
            obj_entity = content_dict[item_key][order_num]
            if (item_key == 'titles') or (item_key == 'integers'):
                obj_dict[item_key[:-1]] = obj_entity.strip()
            else:
                obj_dict[item_key[:-1]] = obj_entity

