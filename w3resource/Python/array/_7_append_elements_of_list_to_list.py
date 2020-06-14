#7. Write a Python program to append items from inerrable to the end of the array.


def addingToList(nums):
    """
    test text
    """
    need_to_add = nums

    nums.extend(need_to_add)
    return nums



array_num = [1, 3, 5, 7, 9]
result = addingToList(array_num)

for x in result:
    print(x)
    print(addingToList.__doc__)