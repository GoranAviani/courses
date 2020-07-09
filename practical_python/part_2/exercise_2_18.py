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

    print(holdings['IBM'])

    print(holdings.most_common(3))

    portfolio2 = read_portfolio('files/portfolio2.csv')
    holdings2 = Counter()
    for s in portfolio2:
        holdings2[s['name']] += s['shares']

    print(holdings2)

    all_holdings = holdings + holdings2
    print(all_holdings)




if __name__ == '__main__':
    main()

