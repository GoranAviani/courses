

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



if __name__ == '__main__':
    main()