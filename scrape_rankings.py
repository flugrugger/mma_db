from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import csv

with urlopen ('https://www.ufc.com/rankings') as html_file:
	soup = BeautifulSoup(html_file, 'lxml')

with open('ufcRankings_html.txt', 'w') as f: 
	f.write(soup.prettify())

#list containing a list for each weight class with ranking information
everyWeightClass = []

#create a list of html tables, one for each weight class
weightClassRankings = soup.find_all('table', class_="views-table views-view-table cols-0")

#for each weight class, extract the name of the weight class and the champion
for i in weightClassRankings:
	rankingsOfWeightClass = []

	weightClassInfo = i.find('div', class_='info')

	nameOfWeightClass = weightClassInfo.h4.text

	nameOfChampion = weightClassInfo.find('div', class_="views-row").text

	#add the champion to the rankings
	rankingsOfWeightClass += [[0,nameOfChampion]]
	
	rows = i.find_all('tr')
	
	#add the rest of the top 15 to the rankings
	for row in rows:
		columns = row.find_all('td')

		rankingNumber = columns[0].text.strip()

		name = columns[1].a.text.strip()

		rankingsOfWeightClass += [[rankingNumber, name]]

	#add rankings for this weight class to the list of all weight classes
	everyWeightClass += [rankingsOfWeightClass]

	print(rankingsOfWeightClass)
	print()

	with open("rankings/"+nameOfWeightClass+".csv", "w", newline="") as f:
		writer = csv.writer(f)
		writer.writerows(rankingsOfWeightClass)

#print(everyWeightClass)

