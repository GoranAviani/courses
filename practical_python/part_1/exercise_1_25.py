"""
Exercise 1.25: Lists of anything
"""

def main():
    symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,CAT,GOOG'
    symlist = symbols.split(',')
    nums = [101, 102, 103]
    items = ['spam', symlist, nums]
    print(items)
    print(items[0])
    print(items[0][0])
    print(items[1])
    print(items[1][1])
    print(items[1][1][2])
    print(items[2])
    print(items[2][1])


if __name__ == '__main__':
    main()