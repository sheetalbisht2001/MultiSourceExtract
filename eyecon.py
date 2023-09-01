import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver


# the following code snippet helps in getting the name and other data from truecaller provided the trucaller is logged in

driver = webdriver.Chrome()
driver.get('https://www.truecaller.com/search/in/8268291167')

results = []
other_results = []
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

header_opening_tags = soup.find_all('header')


header_tag = header_opening_tags[0]
# Find the <div> elements inside the <header> tag
div_elements_inside_header = header_tag.find_all('div')

# Find the third <div> inside the list of <div> elements
main_div = div_elements_inside_header[0]  


child_divs = main_div.find_all('div')

print(len(child_divs))

name_div = child_divs[2]

print(name_div.text)

