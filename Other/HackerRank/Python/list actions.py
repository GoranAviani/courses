def printing(result):
    intResult = []
    for x in result:
        intResult.append(int(x))
    return intResult

def main():
    n = int(input())
    result = []

    for x in range(0, n):
        userInput = str(input())
        commands = userInput.split(" ")
        if commands[0] == "insert":
            result.insert(int(commands[1]), int(commands[2]))
        elif commands[0] == "print":
            result = printing(result)
            print(result)
        elif commands[0] == "remove":
            result.remove(int(commands[1]))
        elif commands[0] == "append":
            result.append(int(commands[1]))
        elif commands[0] == "sort":
            result = sorted(result)
        elif commands[0] == "pop":
            result.pop()
        elif commands[0] == "reverse":
            result = sorted(result, reverse=True)


if __name__ == "__main__":
    main()
'''
    29
    append
    1
    append
    6
    append
    10
    append
    8
    append
    9
    append
    2
    append
    12
    append
    7
    append
    3
    append
    5
    insert
    8
    66
    insert
    1
    30
    insert
    6
    75
    insert
    4
    44
    insert
    9
    67
    insert
    2
    44
    insert
    9
    21
    insert
    8
    87
    insert
    1
    75
    insert
    1
    48
    print
    reverse
    print
    sort
    print
    append
    2
    append
    5
    remove
    2
    print
'''