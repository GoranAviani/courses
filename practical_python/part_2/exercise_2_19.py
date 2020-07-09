"""
Exercise 2.19: List comprehensions
"""

nums = [1,2,3,4]
squares = []
for x in nums:
    squares.append(x*x)

twice = []
for x in nums:
    twice.append(2*x)

print(squares)
print(twice)

