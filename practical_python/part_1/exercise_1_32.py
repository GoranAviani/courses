"""
Exercise 1.32: Using a library function
"""

import csv

def main():
    f = open('files/portfolio.csv')
    rows = csv.reader(f)
    headers = next(rows)
    print(headers)
    for row in rows:
        print(row)

if __name__ == '__main__':
    main()