"""
Exercise 2.4: A list of tuples
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
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
    return portfolio

def main():
    portfolio = read_portfolio('files/portfolio.csv')
    print(portfolio)

if __name__ == '__main__':
    main()