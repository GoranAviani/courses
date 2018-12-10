

#15. Write a Python program to get the maximum and minimum value in a dictionary.

dicts ={3: 12, 5:7, 8: 2}

maxNum = 0
minNum = 0
gotFirstmin = False
for k,v in dicts.items():
# print(v)
if gotFirstmin == False:
minNum = v
gotFirstmin = True

if v > maxNum:
maxNum = v
if v < minNum:
minNum = v

print(maxNum)
print(minNum)






#2018-12-10
#15. Write a Python program to get the maximum and minimum value in a dictionary.

dic1 = {'x':500,'d':5, 'y':5874, 'z': 560}
minNumv = dic1['x']
maxNumv = dic1['x']
print(str(minNumv))

for k, v in dic1.items():
if v < minNumv:
minNumv = v
elif v > maxNumv:
maxNumv = v

print(str(minNumv))
print(str(maxNumv))

