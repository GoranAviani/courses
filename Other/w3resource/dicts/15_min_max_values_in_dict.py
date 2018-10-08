

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
