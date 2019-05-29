def main():
    n = int(input())
    result = []

    for x in range(0, n):
        userInput = str(input())
        commands = userInput.split(" ")
        if commands[0] == "insert":
            result.insert(int(commands[1]), commands[2])
        elif commands[0] == "print":
            print(result)
        elif commands[0] == "remove":
            result.remove(commands[1])
        elif commands[0] == "append":
            result.append(commands[1])
        elif commands[0] == "sort":
            result = sorted(result)


if __name__ == "__main__":
    main()