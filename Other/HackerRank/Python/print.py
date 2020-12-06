

def main():
    result = ""
    userInput = int(input())
    for x in range(1,userInput+1):
        result = result + str(x)

    print(result)



if __name__ == "__main__":
    main()