import urllib

from bs4 import BeautifulSoup

import pandas as pd

import sys

import unicodedata

import random

import re

import csv
	
#Put all UFC fighter names in a list
def all_fighters():
	wiki = "https://en.wikipedia.org/wiki/List_of_current_UFC_fighters"

	from urllib.request import urlopen

	page = urlopen(wiki)

	soup = BeautifulSoup(page,"lxml")

	all_tables = soup.find_all('table', class_="wikitable")
	
	all_tables = all_tables[8:]
	
	fighter_list = []
	
	for table in all_tables:
		for row in table.findAll("tr"):
			cells = row.findAll("td")
			if len(cells) != 0:
				fighter_name = cells[1].find(text=True)
				#print(fighter_name)
				
				if fighter_name not in fighter_list:
					#For each name in the list
					name = fighter_name.split(', ')
						
					formatted_name = []
						
					#Remove space and replace with underscore
					for i in name:
						if " " in i:
							formatted_name += [i.replace(" ","_")]
						else:
							formatted_name += [i]
					#Concatenate
					if len(formatted_name) != 1: 
						fighter_name = formatted_name[1]+'_'+formatted_name[0]
					else:
						fighter_name = formatted_name[0]
					
				#Clean string
				fighter_name = fighter_name.replace("\n",'')

				fighter_list += [fighter_name]
	
	return fighter_list
	
def random_fighter():
	li = all_fighters()
	
	n = random.randrange(len(li))
	
	
	print(li[n])
	return li[n]
	
#Personal fighter information
def find_data(name):
	data = {}
	
	data['name'] = name
	
	wiki = "https://en.wikipedia.org/wiki/" + name

	from urllib.request import urlopen

	page = urlopen(wiki)

	soup = BeautifulSoup(page, "lxml")
	
	info_table = soup.find('table', class_='infobox vcard')
	
	for row in info_table.findAll("tr"):
		headers = row.find('th')
		tdata = row.find('td')
		if headers:
			#Find the age of the fighter.
			if headers.string == "Born":
				age_data = tdata.find('span', class_="noprint ForceAgeToShow")
				age_str = str(age_data.find(string=True))
				#Use regex to separate the integers
				age_int = int(re.search(r'\d+', age_str).group())
				data['age (yrs)']= age_int
			if headers.string == "Team":
				tdata_str = str(tdata.find(string=True))
				tdata_str = tdata_str.replace('\xa0','')
				data['gym']= tdata_str
			if headers.string == "Weight":
				tdata_str = str(tdata.find(string=True))
				tdata_str = tdata_str.replace('\xa0','')
				tdata_str = re.sub(r'.*([0-9]{3})\s*lb.*',r'\1',tdata_str)
				tdata_str = int(tdata_str)
				data['weight']= tdata_str
			#For height and reach use RegEx to separate inches/cm into to separate items in a list.
			if headers.string == "Height":
				tdata_str = str(tdata.find(string=True))
				tdata_str = tdata_str.replace('\xa0','')
				tdata_str = re.sub(r'(.*ft) (.*in).*\((.*)\)',r'\1\2 \3',tdata_str)
				tdata_str = tdata_str.split(" ")
				data['height']= tdata_str
			if headers.string == "Reach":
				tdata_str = str(tdata.find(string=True))
				tdata_str = tdata_str.replace('\xa0','')
				tdata_str = re.sub(r'(.*in).*\((.*)\)',r'\1 \2',tdata_str)
				tdata_str = tdata_str.split(" ")
				data['reach']= tdata_str
	return data

#MMA Record Information
def find_career(name):
	try:
		wiki = "https://en.wikipedia.org/wiki/" + name

		from urllib.request import urlopen

		page = urlopen(wiki)

		soup = BeautifulSoup(page,"lxml")
		
		right_table = soup.select('table[style="font-size: 85%;"]')

		#Generate lists
		A=[]
		B=[]
		C=[]
		D=[]
		E=[]
		F=[]
		G=[]
		H=[]
		I=[]
		J=[]
		for row in right_table[0].findAll("tr"):
			cells = row.findAll('td')

			if len(cells) == 10: #Only extract table body not heading

				A.append(cells[0].find(text=True))
				B.append(cells[1].find(text=True))
				C.append(cells[2].find(text=True))
				D.append(cells[3].find(text=True))
				E.append(cells[4].find(text=True))
				F.append(cells[5].find(text=True))
				G.append(cells[6].find(text=True))
				H.append(cells[7].find(text=True))
				I.append(cells[8].find(text=True))
				J.append(cells[9].find(text=True))

			for i in [A,B,C,D,E,F,G,H,I,J]:
				i[:] = [s.replace('\n', '') for s in i]

		with open(name+'.csv', 'w') as writeFile:
			writer = csv.writer(writeFile)
			writer.writerow(['Result','Record','Opponent','Method','Event','Date','Round','Time','Location','Notes'])

			for j in range(len(A)):
				row = []
				for i in [A,B,C,D,E,F,G,H,I,J]:
					row += [i[j]]
				writer.writerow(row)

		writeFile.close()

	except IndexError:
		#Try adding "_(fighter)" to the end of the wiki link
		try:
			df = find_career(name+"_(fighter)")
		except:
			print("")
			print("Adding (fighter) didn't work for " + name)
			print("")
	except UnicodeEncodeError:
		#Normalize weird characters
		try:
			normal = unicodedata.normalize('NFKD', name).encode('ASCII', 'ignore')
			normal = normal.decode()
			df = find_career(normal)
		except:
			print("")
			print("Encoding did not work for "+ name)
			print("")

#Add career info of each fighter to a dictionary
def construct_roster(n):
	full_roster = {}
	
	list = all_fighters()
	
	#For each name in the list
	for i in list[:n]:
		try:
			full_name = i
			
			#Find the fighter data from their wiki page
			fighter_data = find_career(full_name)
				
			#Add fighter data to roster dictionary
			full_roster[full_name] = [fighter_data]
				
			print(full_name)
		except IndexError:
			#Try adding "_(fighter)" to the end of the wiki link
			try:
				fighter_data = find_career(full_name+"_(fighter)")
				full_roster[full_name] = [fighter_data]
				print(full_name)
			except:
				print("")
				print("Adding (fighter) didn't work for " + full_name)
				print("")
		except UnicodeEncodeError:
			#Normalize weird characters
			try:
				normal = unicodedata.normalize('NFKD', full_name).encode('ASCII', 'ignore')
				normal = normal.decode()
				
				#Try with normalized characters
				fighter_data = find_career(normal)
				full_roster[full_name] = [fighter_data]
				print(full_name)
			except:
				print("")
				print("Encoding did not work for "+ full_name)
				print("")
		#When all else fails, print ERROR
		except:
			print("")
			print("ERROR -----> "+full_name)
			e = sys.exc_info()[0]
			print(e)
			print("")

	return full_roster
