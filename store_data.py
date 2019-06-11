# run this script to take a list of fighter names, create INSERT statements, and write them to a file

from get_data import *

with open('insert_fighter_stats.txt', 'w') as f: 
	    f.write('USE mma;')

list_of_fighter_names = all_fighters()

for f in list_of_fighter_names:
	try:
		find_data(f)
	except IndexError:
		print('Try adding \"_(fighter)\" to the end of the wiki link')
		try:
			df = find_data(f+"_(fighter)")
		except:
			print("")
			print("Adding (fighter) didn't work for " + f +'. The name of the fighter has been saved to \"uninserted_list\" text')
			print("")

			with open('uninserted_fighters.txt', 'a') as w: 
				w.write(f)
	except UnicodeEncodeError:
		print('Normalize weird characters')
		try:
			normal = unicodedata.normalize('NFKD', f).encode('ASCII', 'ignore')
			normal = normal.decode()
			df = find_data(normal)
		except:
			print("")
			print("Encoding did not work for "+ f +'. The name of the fighter has been saved to \"uninserted_list\" text')
			print("")

			with open('uninserted_fighters.txt', 'a') as w: 
				w.write(f)
	except:
		print('Unexpected error for ' + f + '. The name of the fighter has been saved to \"uninserted_list\" text')
		
		with open('uninserted_fighters.txt', 'a') as w: 
			w.write(f)