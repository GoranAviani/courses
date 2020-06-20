"""
Exercise 1.25: Lists of anything
"""

def main():
    symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,CAT,GOOG'
    symlist = symbols.split(',')
    nums = [101, 102, 103]
    items = ['spam', symlist, nums]
    print(items)

if __name__ == '__main__':
    main()