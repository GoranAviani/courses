#2. Write a Python script to add a key to a dictionary.
#Sample Dictionary : {0: 10, 1: 20}
#Expected Result : {0: 10, 1: 20, 2: 30}

d = {0: 10, 1: 20, 2: 30, 5: 50}
largestKey = 0
print(largestKey)

for k, v in d.items():
    print(k)
    print(v)
    if k > largestKey:
        largestKey = k


print("largest key is {}".format(largestKey))

d[largestKey+1] = 60

for k, v in d.items():
    print(k)
    print(v)