from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
from bs4 import BeautifulSoup


# insert objects to find as list of tuples

class WebScrapingPrototype(object):
    def __init__(self, driver_path, urls, html_tag_object_tuples, object_names, filename):
        self.driver_path = driver_path
        self.urls = urls
        self.objects_to_find = html_tag_object_tuples
        self.object_names = object_names
        self.driver = None
        self.data_arrays = []
        self.series = {}
        self.filename = filename

        # add tests to check that each tuple is a html tag first and tag name last

    def initiate_driver(self):
        s = Service(self.driver_path)
        self.driver = webdriver.Chrome(service=s)

    def scrape(self):
        i = 0
        # iterates through URLs
        while i <= len(urls) - 1:
            self.driver.get(self.urls[i])

            content = self.driver.page_source
            soup = BeautifulSoup(content, features='html.parser')
            
            data_array_i = []
            # print(f'OBJECT NAME ARRAY: {self.object_names[i]}')

            # iterate through each tuple in self.objects_to_find
            # 0 = html tag, 1 = id

            for object_tuple in self.objects_to_find:
                list_tuple = list(object_tuple)
                # print(list_tuple)
                for list_tuple[1] in soup.findAll(attrs={list_tuple[0]: list_tuple[1]}):
                    name_i = list_tuple[1].find(list_tuple[2])
                    # print(name_i)
                    if name_i not in data_array_i:
                        data_array_i.append(name_i.text)
            
            self.data_arrays.append(data_array_i)
            i+=1
            # add error if something isn't found?? how does bs4 handle this
        print(f'DATA ARRAYS: {self.data_arrays}')

    def create_csv(self):
        # dict
        print(f'OBJECT NAMES: {self.object_names}')
        i = 0
        while i <= len(self.data_arrays) - 1:
            series_i = pd.Series(self.data_arrays[i], name= str(self.object_names[i]))
            self.series[self.object_names[i]] = series_i
            i += 1

        df = pd.DataFrame.from_dict(self.series)
        # pd.DataFrame.from_dict for this
        # convert the two lists to dict by index

        df.to_csv(f'{self.filename}.csv', index=False, encoding='utf-8')



if __name__ == '__main__':
    # for testing purposes
    urls = ['http://www.seasky.org/astronomy/astronomy-calendar-2022.html', 'http://www.seasky.org/astronomy/astronomy-calendar-2023.html', 'http://www.seasky.org/astronomy/astronomy-calendar-2024.html', 'http://www.seasky.org/astronomy/astronomy-calendar-2025.html', 'http://www.seasky.org/astronomy/astronomy-calendar-2026.html']
    scraper = WebScrapingPrototype('/Users/maliabarker/Desktop/main/MakeSchool/Term4/ACS_2511/chromedriver', 
                                    urls, 
                                    [('class', 'b1', 'p'), ('class', 'b2', 'p'), ('class', 'b3', 'p'), ('class', 'b4', 'p'), ('class', 'b5', 'p'), ('class', 'b8', 'p'), ('class', 'b9', 'p')],
                                    ['new_moons', 'full_moons', 'lunar_eclipses', 'solar_eclipses', 'planetary_events', 'equinox_solstice', 'meteor_showers'],
                                    'celestial_events')

    s = Service('/Users/maliabarker/Desktop/main/MakeSchool/Term4/ACS_2511/chromedriver')
    driver = webdriver.Chrome(service=s)
    scraper.initiate_driver()
    scraper.scrape()
    scraper.create_csv()