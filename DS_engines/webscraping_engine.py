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
        self.data_arrays = None
        self.series = None
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

            self.object_names[i] = []

            # iterate through each tuple in self.objects_to_find
            # 0 = html tag, 1 = id

            for object_tuple in self.objects_to_find:
                for object_tuple[1] in soup.findAll(attrs={object_tuple[0]: object_tuple[1]}):
                    name_i = object_tuple[1].find()
                    # TODO: add attribute for    ^^   so i know what to find within this tuple condition
                    if name_i not in self.object_names[i]:
                        self.object_names[i].append(name_i.text)
            
            self.data_arrays.append(self.object_names[i])
            i+=1
            # add error if something isn't found?? how does bs4 handle this

    def create_csv(self):
        i = 0
        while i <= len(self.data_arrays) - 1:
            series_i = pd.Series(self.object_names[i], name= str(self.object_names[i]))
            self.series.append(series_i)
            i += 1

        # TODO: How do I create the code below iteratively?
        df = pd.DataFrame({'NewMoons': series0, 'FullMoons': series1, 'LunarEclipses': series2, 'SolarEclipses': series3, 'PlanetaryEvents': series4, 'EquinoxesSolstices': series5, 'MeteorShowers': series6})
        
        df.to_csv(f'{self.filename}.csv', index=False, encoding='utf-8')





s = Service('/Users/maliabarker/Desktop/main/MakeSchool/Term4/ACS_2511/chromedriver')
driver = webdriver.Chrome(service=s)

urls = ['http://www.seasky.org/astronomy/astronomy-calendar-2022.html', 'http://www.seasky.org/astronomy/astronomy-calendar-2023.html', 'http://www.seasky.org/astronomy/astronomy-calendar-2024.html', 'http://www.seasky.org/astronomy/astronomy-calendar-2025.html', 'http://www.seasky.org/astronomy/astronomy-calendar-2026.html']

new_moons = []
full_moons = []
lunar_eclipses = []
solar_eclipses = []
planetary_events = []
equinox_solstice = []
meteor_showers = []

i = 0

while i <= len(urls) - 1:
    driver.get(urls[i])

    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")

    for b1 in soup.findAll(attrs={'class': 'b1'}):
        # for new moons
        name = b1.find('p')
        if name not in new_moons:
            new_moons.append(name.text)

    for b2 in soup.findAll(attrs={'class': 'b2'}):
        # for full moons
        name1 = b2.find('p')
        if name1 not in full_moons:
            full_moons.append(name1.text)

    for b3 in soup.findAll(attrs={'class': 'b3'}):
        # for lunar eclipses
        name2 = b3.find('p')
        if name2 not in lunar_eclipses:
            lunar_eclipses.append(name2.text)

    for b4 in soup.findAll(attrs={'class': 'b4'}):
        # for solar eclipses
        name3 = b4.find('p')
        if name3 not in solar_eclipses:
            solar_eclipses.append(name3.text)

    for b5 in soup.findAll(attrs={'class': 'b5'}):
        # for planetary events
        name4 = b5.find('p')
        if name4 not in planetary_events:
            planetary_events.append(name4.text)

    for b8 in soup.findAll(attrs={'class': 'b8'}):
        # for equinoxes and solstices
        name5 = b8.find('p')
        if name5 not in equinox_solstice:
            equinox_solstice.append(name5.text)

    for b9 in soup.findAll(attrs={'class': 'b9'}):
        # for meteor showers
        name6 = b9.find('p')
        if name6 not in meteor_showers:
            meteor_showers.append(name6.text)
    
    i+=1


series0 = pd.Series(new_moons, name = 'NewMoons')
series1 = pd.Series(full_moons, name = 'FullMoons')
series2 = pd.Series(lunar_eclipses, name = 'LunarEclipses')
series3 = pd.Series(solar_eclipses, name = 'SolarEclipses')
series4 = pd.Series(planetary_events, name = 'PlanetaryEvents')
series5 = pd.Series(equinox_solstice, name = 'EquinoxesSolstices')
series6 = pd.Series(meteor_showers, name = 'MeteorShowers')

df = pd.DataFrame({'NewMoons': series0, 'FullMoons': series1, 'LunarEclipses': series2, 'SolarEclipses': series3, 'PlanetaryEvents': series4, 'EquinoxesSolstices': series5, 'MeteorShowers': series6})
df.to_csv('celestial_events.csv', index=False, encoding='utf-8')

if __name__ == '__main__':
    # for testing purposes
    for x in meteor_showers:
        print(x)