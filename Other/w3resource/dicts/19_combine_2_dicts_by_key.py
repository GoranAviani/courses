

#19. Write a Python program to combine two dictionary adding values for common keys. Go to the editor
#d1 = {'a': 100, 'b': 200, 'c':300}
#d2 = {'a': 300, 'b': 200, 'd':400}
#Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

result ={}
for x in d1:
	for y in d2:
		if x == y:
			result[x] = d1[x] + d2[y]

for x in d1:
	if x not in result:
		result[x] = d1[x]

for x in d2:
	if x not in result:
		result[x] = d2[x]


print(result)
