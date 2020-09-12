"""
 Determine whether the sequence of elements items is ascending so that its each element is strictly larger than (and not merely equal to) the element that precedes it.

Input: Iterable with ints.

Output: Bool.

Example:
is_ascending([-5, 10, 99, 123456]) == True
is_ascending([99]) == True
is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
is_ascending([]) == True
is_ascending([1, 1, 1, 1]) == False
"""