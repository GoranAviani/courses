"""
Exercise 1.14: String concatenation
"""

def main():
    symbols = 'AAPL,IBM,MSFT,YHOO,SCO'
    symbols += ', GOOG'
    symbols = 'HPQ, ' + symbols

    print(symbols)
if __name__ == '__main__':
    main()