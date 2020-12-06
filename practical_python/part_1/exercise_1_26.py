"""
Exercise 1.26: File Preliminaries
"""
def main():
    with open('files/portfolio.csv', 'rt') as f:
        data = f.read()
        print(data)

        for line in f:
            print(line, end='')

    f = open('files/portfolio.csv', 'rt')
    headers = next(f)
    print(headers)

    for line in f:
        print(line, end='')
    f.close()


    f = open('files/portfolio.csv', 'rt')
    headers = next(f).split(',')
    print(headers)
    for line in f:
        row = line.split(',')
        print(row)

if __name__ == '__main__':
    main()