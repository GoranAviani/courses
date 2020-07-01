"""
Exercise 2.17: Inverting a dictionary
"""

prices = {
        'GOOG' : 490.1,
        'AA' : 23.45,
        'IBM' : 91.1,
        'MSFT' : 34.23
    }


print(prices.items())


pricelist = list(zip(prices.values(),prices.keys()))
print(pricelist)

print(min(pricelist))
print(max(pricelist))

print(sorted(pricelist))


a = [1, 2, 3, 4]
b = ['w', 'x', 'y', 'z']
c = [0.2, 0.4, 0.6, 0.8]
print(list(zip(a, b, c)))


a = [1, 2, 3, 4, 5, 6]
b = ['x', 'y', 'z']
print(list(zip(a,b)))