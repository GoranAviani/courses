#12. Write a Python program to remove the first occurrence of a specified element from an array.


def removeOccur(array_num):
    position = 0
    for x in array_num:
        position += 1
        if x == num:
            array_num.pop(position)








num = 3
array_num = [1, 3, 5, 3, 7, 1, 9, 3]
removeOccur(array_num, num)