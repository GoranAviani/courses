"""
Exercise 1.5: The Bouncing Ball
"""
def main():
    height = 100
    #next_heights = []
    for x in range(1, 11):
        height = height * 3 / 5
        print("{}, {}" .format(x, height))
    #Printing is possible while the fun is executing
    #for result in next_heights:
    #    print(result)
if __name__ == '__main__':
    main()