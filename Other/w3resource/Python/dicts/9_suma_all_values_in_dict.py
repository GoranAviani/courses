#Write a Python program to sum all the items in a dictionary.

sums = 0
dict1 = {"num" : 12, "kis" : 3, "ris" : 5}

for k, v in dict1.items():
    sums += v

print(str(sums))