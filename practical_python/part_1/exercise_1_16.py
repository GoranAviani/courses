"""
Exercise 1.16: String Methods
"""



def main():
    symbols = 'AAPL,IBM,MSFT,YHOO,SCO'
    symbols += ', GOOG'
    symbols = 'HPQ, ' + symbols

    print(symbols)

    print(symbols.lower())
    lowersyms = symbols.lower()
    print(lowersyms)
    v1 = symbols.find('MSFT')
    print(v1)
    symbols = symbols.replace('SCO', 'DOA')
    print(symbols)

    name = '   IBM   \n'
    name = name.strip()
    print(name)

if __name__ == '__main__':
    main()