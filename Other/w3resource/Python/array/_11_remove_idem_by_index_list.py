#11. Write a Python program to remove a specified item using the index from an array.


def removeByIndex(array_num, index):
    array_num.pop(index-1)
    return array_num


index = 3
array_num = [1, 3, 5, 7, 9]
result = removeByIndex(array_num, index)
for x in result:
    print(x)
