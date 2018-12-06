#Write a Python program to remove a key from a dictionary.


#remove c
dict1 = {"a" : 2, "b" : 3, "c" : 1, "d" : 4}
result = {}

for k, v in dict1.items():
    if k == 'c':
        continue
    else:
        result[k] = v


print( "result it {}" . format(result))


dict2 = {"a" : 2, "b" : 3, "c" : 1, "d" : 4}
if "c" in dict2:
    del dict2["c"]

print(dict2)