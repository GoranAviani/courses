"""
Exercise 2.6: Dictionaries as a container
"""

prices = { }
prices['IBM'] = 92.45
prices['MSFT'] = 45.12
print(prices)
print(prices['IBM'])
try:
    aapl = prices['AAPL']
except KeyError as e:
    print("Object not found: " + str(e))
is_found = 'AAPL' in prices
print(is_found)