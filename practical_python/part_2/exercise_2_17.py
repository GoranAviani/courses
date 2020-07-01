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