from get_data import *

def has_fought(f1,f2):
	f1_career = find_career(f1)
	
	f2 = f2.replace("_"," ")
	
	for i in f1_career["Opponent"]:
		if f2 == i:
			return True
	
	return False
	
def num_fights(f1):
	f1_career = find_career(f1)
	
	return len(f1_career)
	
def win_percentage(f1):
	f1_career = find_career(f1)
	
	wins = 0
	
	for i in f1_career["Result"]:
		if i == "Win":
			wins += 1
			
	return float(wins/len(f1_career))

def percentage_by_dec(f1):
	f1_career = find_career(f1)
	
	dec = 0
	
	for i in f1_career["Method"]:
		if "Decision" in i:
			dec += 1
			
	return float(dec/len(f1_career))
	
def percentage_by_ko(f1):
	f1_career = find_career(f1)
	
	kos = 0
	
	for i in f1_career["Method"]:
		if "KO" in i:
			kos += 1
			
	return float(kos/len(f1_career))
	
def percentage_by_sub(f1):
	f1_career = find_career(f1)
	
	subs = 0
	
	for i in f1_career["Method"]:
		if "Submission" in i:
			subs += 1
			
	return float(subs/len(f1_career))
	
def profile(f1):
	data = find_data(f1)
	psub = percentage_by_sub(f1)
	pko = percentage_by_ko(f1)
	pdec = percentage_by_dec(f1)
	n = num_fights(f1)
	
	print(data)
	print(str(n) + " fights")
	print(str(pdec) + " % Decision")
	print(str(pko) + " % KO")
	print(str(psub) + " % Submission")
	
def watch_this(f1):
	f1_career = find_career(f1)
	
	opponent = 'n/a'
	
	count = random.randrange(len(f1_career))
	
	barn_burner = input("Choose a FOTN/POTN fight? (Y/N)\n")
	
	if barn_burner == 'Y':
		for i in f1_career["Notes"]:
			if i != None and opponent == 'n/a':
				if ("Performance of the Night" in i) or ("Fight of the Night" in i):
					opponent = f1_career["Opponent"][count]
					
					time_spoiler = input("Give the duration of the bout? (Y/N)\n")
					
					if time_spoiler == 'Y':
						#Calculate length of the bout
						time = f1_career["Time"][count]
						round = f1_career["Round"][count]
						
						time_li = time.split(":")
						total_min = int(time_li[0]) + ((int(round)-1)*5)
						total_sec = time_li[1]
						
						total_duration = "The bout was " + str(total_min) + " min and " + str(total_sec) + " sec long."
						print(total_duration)
					
					matchup = f1 + " vs. " + opponent
			if count == len(f1_career) - 1:
				count = 0
			else:
				count += 1
		if opponent == 'n/a':
			matchup = watch_this(random_fighter())
	elif barn_burner == 'N':
		count = random.randrange(len(f1_career))
		opponent = f1_career["Opponent"][count]
		matchup = f1 + " vs. " + opponent
		
		time_spoiler = input("Give the duration of the bout? (Y/N)\n")
					
		if time_spoiler == 'Y':
			#Calculate length of the bout
			time = f1_career["Time"][count]
			round = f1_career["Round"][count]
			
			time_li = time.split(":")
			total_min = int(time_li[0]) + ((int(round)-1)*5)
			total_sec = time_li[1]
			
			total_duration = "The bout was" + str(total_min) + " min and " + str(total_sec) + " sec long."
			print(total_duration)
	
	return matchup