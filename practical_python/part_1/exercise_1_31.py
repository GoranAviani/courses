"""
Exercise 1.31: Error handling
"""

def portfolio_cost():
    total_value = 0
    value_by_line = 0
    with open('files/missing.csv', 'rt') as f:
        headers = next(f)
        for line in f:
            row = line.split(',')
            try:
                value_by_line = int(row[1]) * float(row[2])
                total_value += value_by_line
            except:
                pass
    print(total_value)

def main():
    portfolio_cost()

if __name__ == '__main__':
    main()