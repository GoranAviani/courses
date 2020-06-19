def main():
    starting_height = 100
    next_heights = []
    for x in range(10):
        starting_height = starting_height * 3 / 5
        next_heights.append(starting_height)

    for result in next_heights:
        print(result)
if __name__ == '__main__':
    main()