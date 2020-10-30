"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the
first and last elements of the given list. For practice, write this code inside a function.
"""

a = [5, 10, 15, 20, 25]
result = []
result.append(a[0])
result.append(a[len(a)-1])
print(result)