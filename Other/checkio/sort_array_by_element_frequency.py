'''
 Sort the given iterable so that its elements end up in the decreasing frequency order,
 that is, the number of times they appear in elements. If two elements have the same
  frequency, they should end up in the same order as the first appearance in the iterable.

Input: Iterable

Output: Iterable

Example:
frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]) == [4, 4, 4, 4, 6, 6, 2, 2]
frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']) == ['bob', 'bob', 'bob', 'carl', 'alex']
1
2

Precondition: elements can be ints or strings
'''

def frequency_sort(list_to_sort):
    """
    for every element in list_to_sort:
    save its frequency in one dict and order they are coming in (only once in another dict)

    """

    result = []
    frequency_of_items = {}
    order_of_items = {}
    order_counter = 0
    for element in list_to_sort:
        if element not in frequency_of_items:
            frequency_of_items[element] = 1
        else:
            frequency_of_items[element] += 1

        if element not in order_of_items:
            order_counter += 1
            order_of_items[element] = order_counter

    for k, v in frequency_of_items.items():
        sub_result = []
        for x in range(0, v):
            sub_result.append(k)
        result.extend(sub_result)
    return result

def main():
    # These "asserts" are used for self-checking and not for testing
    assert frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert frequency_sort(['bob', 'bob', 'carl', 'carl', 'alex', 'bob', 'carl']) == ['bob', 'bob', 'bob', 'carl',
                                                                                     'carl', 'carl', 'alex']
    assert frequency_sort(['carl', 'bob', 'bob', 'carl', 'alex']) == ['carl', 'carl', 'bob', 'bob', 'alex']

    print("success!")


if __name__ == "__main__":
    main()