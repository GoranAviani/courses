"""
Exercise 2.2: Dictionaries as a data structure
"""

def main():
    row = ['AA', 100, 32.2]
    d = {
        'name': row[0],
        'shares': int(row[1]),
        'price': float(row[2])
    }
    print(d)

    cost = d['shares'] * d['price']
    print(f'{cost:0.2f}')

if __name__ == '__main__':
    main()