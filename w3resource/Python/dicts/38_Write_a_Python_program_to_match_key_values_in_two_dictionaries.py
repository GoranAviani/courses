"""
38. Write a Python program to match key values in two dictionaries. Go to the editor
Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
Expected output: key1: 1 is present in both x and y
"""

list1 = {'key1': 1, 'key2': 3, 'key3': 2}
list2 = {'key1': 1, 'key2': 2}

result = []
for key1, value1 in list1.items():
    for key2, value2 in list2.items():
        if key1 == key2 and value1 == value2:
            result.append(key1)

print(result)