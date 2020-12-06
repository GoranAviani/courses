"""
Exercise 1.22: Appending, inserting, and deleting items
"""
def main():
    symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,CAT,GOOG'
    symlist = symbols.split(',')
    symlist.append('RHT')
    symlist.insert(1, 'AA')
    symlist.remove('MSFT')
    symlist.append('YHO')
    pos = symlist.index('YHOO')
    symlist.remove(symlist[4])
    print(pos)
    print(symlist)


if __name__ == '__main__':
    main()