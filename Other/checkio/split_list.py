'''
ou have to split a given array into two arrays.
If it has an odd amount of elements, then the first array should have more elements.
If it has no elements, then two empty arrays should be returned.

Input: Array.

Output: Array or two arrays.

Example:
split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
split_list([1, 2, 3]) == [[1, 2], [3]]
1
2

'''

import math

def split_list(list_to_split):
    result = []
    element_list = []
    number_of_elements = len(list_to_split)
    split_number = number_of_elements / 2

    if number_of_elements % 2 == 0:
        split_number = int(split_number)
    else:
        split_number = math.ceil(split_number)


    for x in range(0, split_number):
        element_list.append(list_to_split[x])
    result.append(element_list)

    element_list = []
    for x in range(split_number, number_of_elements):
        element_list.append(list_to_split[x])
    result.append(element_list)

    return result

def main():
    print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6]))

    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]

    print("Success!")


if __name__ == "__main__":
    main()