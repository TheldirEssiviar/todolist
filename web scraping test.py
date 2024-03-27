import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Firefox()

driver.get('https://xkcd.com')
results = []

content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
for element in soup.find_all(attrs = {'class': 'title'}):
    name = a.find('a')
    if name not in results:
        results.append(name.text)

for x in results:
    print(x)
