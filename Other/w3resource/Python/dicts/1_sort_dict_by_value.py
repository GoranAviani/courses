#1. Write a Python script to sort (ascending and descending) a dictionary by value.
#my impro:

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

res_asc = []
for x in d:
    print(d[x])
    res_asc.append(d[x])
print("#####")
res_asc.sort()
#for x in res_asc:
#    print(x)
#print("####")

for z in res_asc:
    print("{}: {} ".format(z, d[z]))
print("####")
#descending:
res_asc = res_asc[::-1]
for x in res_asc:
    print(x)

for y in res_asc:
    print("{}: {}".format(y, d[y]))