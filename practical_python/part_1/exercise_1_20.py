"""
Exercise 1.20: Looping over list items
"""


def main():
    symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'
    symlist = symbols.split(',')

    for s in symlist:
        print('s =', s)

if __name__ == '__main__':
    main()