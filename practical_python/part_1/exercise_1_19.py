

def main():
    symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'
    symlist = symbols.split(',')
    print(symlist[0])
    print(symlist[1])
    print(symlist[-1])
    print(symlist[-2])

    symlist[2] = 'AIG'
    print(symlist)


    slice1 = symlist[0:3]
    print(slice1)
    slice2 = symlist[-2:]
    print(slice2)

    mysyms = []
    mysyms.append('GOOG')
    print(mysyms)


    """
    When you do this, the list on the left-hand-side (symlist) will be resized as appropriate to make the 
    right-hand-side (mysyms) fit. For instance, in the above example, 
    the last two items of symlist got replaced by the single item in the list mysyms.
    """
    symlist[-2:] = mysyms
    print(symlist)


if __name__ == '__main__':
    main()