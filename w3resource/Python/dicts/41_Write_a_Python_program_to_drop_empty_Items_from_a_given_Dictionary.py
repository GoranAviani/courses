"""
41. Write a Python program to drop empty Items from a given Dictionary. Go to the editor
Original Dictionary:
{'c1': 'Red', 'c2': 'Green', 'c3': None}
New Dictionary after dropping empty items:
{'c1': 'Red', 'c2': 'Green'}
"""

dict1 = {'c1': 'Red', 'c2': 'Green', 'c3': None}

result = {}
for x, y in dict1.items():
    if y != None:
        result[x] = y

print(result)