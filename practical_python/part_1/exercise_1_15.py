"""
Exercise 1.15: Membership testing (substring testing)
"""


def main():
    symbols = 'AAPL,IBM,MSFT,YHOO,SCO'
    symbols += ', GOOG'
    symbols = 'HPQ, ' + symbols

    print(symbols)

    x =  'IBM' in symbols
    print(x)
    y = 'AA' in symbols
    print(y)
    z = 'CAT' in symbols
    print(z)



if __name__ == '__main__':
    main()