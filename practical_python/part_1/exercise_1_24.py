"""
Exercise 1.24: Putting it all back together
"""

def main():
    symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,CAT,GOOG'
    symlist = symbols.split(',')

    result = ','.join(symlist)
    print(result)
    result = ':'.join(symlist)
    print(result)
    result = ''.join(symlist)
    print(result)

if __name__ == '__main__':
    main()