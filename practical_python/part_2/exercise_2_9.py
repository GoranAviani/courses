"""
Exercise 2.9: Collecting Data
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

def make_report(portfolio, prices):
    report = []
    for port in portfolio:
        old_value = port['shares'] * port['price']
        if port['name'] in prices:
            new_value = port['shares'] * float(prices[port['name']])
            diff_value = old_value - new_value
        else:
            diff_value = old_value

        report.append((port['name'], port['shares'], diff_value))

    print(report)




def main():

    portfolio = read_portfolio('files/portfolio.csv')
    print(portfolio)

    prices = read_prices('files/prices.csv')
    print(prices)

    make_report(portfolio, prices)


if __name__ == '__main__':
    main()