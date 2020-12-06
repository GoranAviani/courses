"""
Exercise 1.23: Sorting
"""


def main():
    symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,CAT,GOOG'
    symlist = symbols.split(',')
    symlist.sort()
    print(symlist)
    symlist.sort(reverse=True)
    print(symlist)

if __name__ == '__main__':
    main()