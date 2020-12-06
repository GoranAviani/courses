"""
Exercise 1.13: Extracting individual characters and substrings
"""


def main():
    symbols = 'AAPL,IBM,MSFT,YHOO,SCO'
    print(symbols[0])
    print(symbols[1])
    print(symbols[2])
    print(symbols[-1])
    print(symbols[-2])

    try:
        symbols[0] = 'a'
    except TypeError as e:
        print(e)

if __name__ == '__main__':
    main()