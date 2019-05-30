from getFighterData import *

from roster import *

import os

roster = construct_roster(5)

for i in roster:
	roster[i].to_csv(os.path.join("C:\\Users\\Ramtin\\Desktop\\mma data\\fighters",i+".txt"),encoding='utf-8')
	
#To read back files store the following code inside a variable
#pd.read_csv('name of fighter',encoding=utf-8')