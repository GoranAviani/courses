#6. Write a Python program to get the number of occurrences of a specified element in an array.
from array import *
array_num = [1, 3, 5, 3, 7, 9, 3]



def print_occurrences(array_num, num):
    counter = 0
    for x in array_num:
        if x == num:
            counter += 1

    print("number of occurring {} is {}.".format(num, counter))


print_occurrences(array_num, 3)
print_occurrences(array_num, 7)
