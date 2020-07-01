"""
Exercise 2.14: More sequence operations
"""

def main():
    data = [4, 9, 1, 25, 16, 100, 49]
    print(min(data))
    print(max(data))
    print(sum(data))

    for x in data:
        print(x)

    for n, x in enumerate(data):
        print(n, x)

    for n in range(len(data)):
            print(data[n])

if __name__ == '__main__':
    main()