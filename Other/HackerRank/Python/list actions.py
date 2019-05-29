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