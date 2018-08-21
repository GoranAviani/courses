#Write a Python program to iterate over dictionaries using for loops.

exdict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

for k, v in exdict.items():
    print("{}: {}".format(k,v))