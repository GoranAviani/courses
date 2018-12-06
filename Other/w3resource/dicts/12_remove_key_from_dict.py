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
