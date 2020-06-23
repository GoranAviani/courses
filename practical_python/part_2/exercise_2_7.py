"""
Exercise 2.6: Dictionaries as a container
"""

import csv

def read_portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    total_cost = 0.0
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {'name': row[0], 'shares': int(row[1]), 'price': float(row[2])}
            portfolio.append(holding)
    return portfolio


def read_prices(filename):
    result = {}
    f = open(filename, 'r')
    rows = csv.reader(f)
    for row in rows:
        try:
            result[row[0]] = row[1]
        except:
            pass
    return result

def main():

    portfolio = read_portfolio('files/portfolio.csv')
    print(portfolio)

    prices = read_prices('files/prices.csv')
    print(prices)


    #old value
    old_value = 0
    for row in portfolio:
        old_pair_value = row['shares'] * row['price']
        old_value += old_pair_value
    print("Old value: {}".format(old_value))

    #current value with new prices
    value = 0
    for x in portfolio:
        for k, v in prices.items():
            if x['name'] == k:
                pair_value = x['shares'] * float(v)
                value += pair_value
    print("Current value: {}". format(value))


if __name__ == '__main__':
    main()