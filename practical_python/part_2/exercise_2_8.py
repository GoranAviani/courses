"""
Exercise 2.8: How to format numbers
"""

def main():
    value = 42863.1
    print(value)
    print(f'{value:0.4f}')
    print(f'{value:>16.2f}')

    print(f'{value:<16.2f}')
    print(f'{value:*>16,.2f}')

    print('%0.4f' % value)
    print('%16.2f' % value)

    f = '%0.4f' % value
    print(f)

if __name__ == '__main__':
    main()