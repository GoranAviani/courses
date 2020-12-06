"""
Exercise 1.17: f-strings
"""

def main():
    name = 'IBM'
    shares = 100
    price = 91.1
    text = f'{shares} shares of {name} at ${price:0.2f}'
    print(text)

if __name__ == '__main__':
    main()