from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen

with urlopen ('https://www.ufc.com/rankings') as html_file:
	soup = BeautifulSoup(html_file, 'lxml')

with open('ufcRankings_html.txt', 'w') as f: 
	f.write(soup.prettify())

#create a list of html tables, one for each weight class
weightClassRankings = soup.find_all('table', class_="views-table views-view-table cols-0")

#for each weight class, extract the name of the weight class and the champion
for i in weightClassRankings:

	weightClassInfo = i.find('div', class_='info')

	nameOfWeightClass = weightClassInfo.h4.text

	print(nameOfWeightClass)

	nameOfChampion = weightClassInfo.find('div', class_="views-row").text

	print(nameOfChampion)

	print()

