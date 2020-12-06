"""
Exercise 1.33: Reading from the command line
"""

import sys

def portfolio_cost(filename):
    total_value = 0
    value_by_line = 0
    with open(filename, 'rt') as f:
        headers = next(f)
        for line in f:
            row = line.split(',')
            try:
                value_by_line = int(row[1]) * float(row[2])
                total_value += value_by_line
            except ValueError as e:
                print("{} . Line: {}" .format(e, line))
                pass
    return total_value

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'files/portfolio.csv'

    cost = portfolio_cost(filename)
    print('Total cost:', cost)

if __name__ == '__main__':
    main()
