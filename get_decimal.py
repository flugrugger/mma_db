#want 6.1
list = [6,1,3,4,5]

sum = 0

for i in list:
	if list.index(i) == 0:
		sum += i
	else:
		sum += (i*(10**-list.index(i)))

print(sum)