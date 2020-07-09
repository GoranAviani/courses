"""
Exercise 2.18: Tabulating with Counters
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

def main():
    portfolio = read_portfolio('files/portfolio.csv')
    print(portfolio
          )
    from collections import Counter
    holdings = Counter()
    for s in portfolio:
        holdings[s['name']] += s['shares']
    print(holdings)

if __name__ == '__main__':
    main()

