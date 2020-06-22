"""
Exercise 2.3: Some additional dictionary operations
"""

def main():
    row = ['AA', 100, 32.2]
    d = {
        'name': row[0],
        'shares': int(row[1]),
        'price': float(row[2])
    }
    d['date'] = (6, 11, 2007)
    d['account'] = 12345

    for k in d:
        print('k =', k)

    for k in d:
        print(k, '=', d[k])

    keys = d.keys()
    print(keys)

    del d['account']
    print(keys)

    items = d.items()
    print(items)
    for k, v in d.items():
        print(k, '=', v)

    print(items)
    d = dict(items)
    print(d)


if __name__ == '__main__':
    main()