"""

"""


def main():
    row = ['AA', 100, 32.2]
    t = (row[0], int(row[1]), float(row[2]))
    print(t)

    cost = t[1] * t[2]
    print(f'{cost:0.2f}')

    t = (t[0], 75, t[2])
    print(t)

    name, shares, price = t
    print(name)
    print(shares)
    print(price)

    t = (name, 2 * shares, price)
    print(t)


if __name__ == '__main__':
    main()