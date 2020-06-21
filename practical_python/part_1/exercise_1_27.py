"""
Exercise 1.27: Reading a data file
"""

def main():
    total_value = 0
    value_by_line = 0
    with open('files/portfolio.csv', 'rt') as f:
        headers = next(f)
        for line in f:
            row = line.split(',')
            value_by_line = int(row[1]) * float(row[2])
            total_value += value_by_line

    print(total_value)

if __name__ == '__main__':
    main()