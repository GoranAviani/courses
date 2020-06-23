"""
Exercise 2.5: List of Dictionaries
"""

import csv
from pprint import pprint

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

def main():
    portfolio = read_portfolio('files/portfolio.csv')
    print(portfolio)

    print(portfolio[0])
    print(portfolio[1])
    print(portfolio[0]['shares'])

    total = 0.0
    for s in portfolio:
        total += s['shares'] * s['price']

    print(total)

    pprint(portfolio)


if __name__ == '__main__':
    main()