"""
Create a program that asks the user for a number and then prints out a list of all
the divisors of that number. (If you don’t know what a divisor is, it is a number that
 divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13
 has no remainder.)
"""

result = []
user_input = input (" enter a num: ")
user_input = int(user_input)
list_to_search = list(range(1, user_input + 1))

print(list_to_search)
for x in list_to_search:
    if user_input % x == 0:
        result.append(x)

print(result)