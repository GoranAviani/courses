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


if __name__ == "__main__":
    main()