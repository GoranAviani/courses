
def main():
    with open('files/portfolio.csv', 'rt') as f:
        data = f.read()
        print(data)

        for line in f:
            print(line, end='')


if __name__ == '__main__':
    main()