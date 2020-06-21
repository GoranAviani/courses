"""
Exercise 1.28: Other kinds of "files"
"""

import gzip

def main():
    with gzip.open('files/portfolio.csv.gz', 'rt') as f:
        for line in f:
            print(line, end='')

if __name__ == '__main__':
    main()