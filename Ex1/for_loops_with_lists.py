spam = list(range(0, 100, 2))

supplies = ['pens', 'staplers', 'flame-throwers', 'binders']

for i in range(len(supplies)):
	print('index ' + str(i) + ' in supplies is: ' + supplies[i])


cat = ['fat', 'orange', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]

# Multiple assignment trick
size, color, disposition = cat