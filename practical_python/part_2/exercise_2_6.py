"""
Exercise 2.6: Dictionaries as a container
"""

import csv

def read_prices(filename):
    result = {}
    f = open(filename, 'r')
    rows = csv.reader(f)
    for row in rows:
        print(row)
        try:
            result[row[0]] = row[1]
        except:
            pass
    return result

def main():
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

    prices1 = read_prices('files/prices.csv')
    print(prices1)
    print(prices1['IBM'])
    print(prices['MSFT'])


if __name__ == '__main__':
    main()