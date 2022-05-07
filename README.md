# THE ULTIMATE BEGINNER DS UTILITY BELT
<br>

## Included: <br>

**DS Prototypic Engines** <br>

1. Analysis Engine - Some basics to start analysis including null value imputation and processing, basic statistical information, structure for some comparative analytical questions, and creating and saving data dictionaries (with numerical encoding needed for visualization)

*NOTE: This analysis engine works directly with the following visualization engine, and will need to be instantiated to use with the visualization engine.* <br>

<br>

2. Visualization Engine - Some basic visualizations, including scatter plots and bar graphs to match certain analysis questions from the analysis engine. Also includes a normal distribution function.<br>
<br>

3. Web Scraping Engine - You will need to download a chromedriver for this engine. Make sure that the driver version and your currenT version of chrome match. Go to https://chromedriver.chromium.org/downloads for downloads and more information. <br> 
Parameters, in order, are:
  1. Driver Path (string): This is the path to the chrome driver. If you cannot find the path, use `which chromedriver` in your terminal. *Note: If the chromedriver will not open and you get an error from your mac along the lines of 'cannot detect for malware', use the command `xattr -d com.apple.quarantine /usr/local/bin/chromedriver` in your terminal to lift this mac quarantine*
  2. Urls (list of strings): This is a list of urls you want to scrape. Make sure to check the 'view page source' from Chrome to see if your information can be easily scraped!
  3. HTML Tag Object Tuples (list of tuples): This parameter may be the most confusing. These are the guidelines dictating what *exactly* you are scraping in terms of HTML tags. Let's say you were scraping names from a site. All the names were under div tags with `class = person_names`. Within that div, there is a p tag that contains the actual name text. So, you would start with the first two parameters, which are going to be the parent div and how it is classified. Then, you include the actual tag you want to scrape data from. EXAMPLE: `('class', 'person_names', 'p')`. Remember, **_these have to be strings_**.
  4. Object Names (list of strings): This will be the name of the columns that eventually go into the CSV file. So, for example, if you're scraping for names, ages, and addresses, you would pass in `['names', 'ages', 'addresses']`. **_IMPORTANT: The order of object names HAS to match the order of tuples you pass in before this. So if index 0 of object names is 'names', then index 0 of HTML tag object tuples needs to be the tuple that dictates the scrape for names data. The data from the tuple will correspond to the matching index in the object name list, which will become the column name in the CSV file created._**
  5. Filename (string): This is the name of the CSV file you want to save.

  To use, instantiate the web scraping object. Use `WebScrapingPrototype.initiate_driver()` to start the driver, `WebScrapingPrototype.scrape()` to actually scrape info, and `WebScrapingPrototype.create_csv()` to save the data as a CSV file. You need to use all of these methods to actually see the data that is scraped.
<br>

**Helper Functions** <br>

1. Import all your data analysis and visualization needs. Includes numpy, pandas, matplotlib, seaborn, scikit-learn, and more! <br>
<br>

2.

3.

4.

5.

6.
<br>

**Glossary** <br>

Includes terms that I just can't seem to remember. Mostly statistical test information.


*Note: All of the libraries used in this repository are included in `requirements.txt`. If using this repo, ignore the import libraries helper function and just download the `requirements.txt` file. Happy data exploration!*

