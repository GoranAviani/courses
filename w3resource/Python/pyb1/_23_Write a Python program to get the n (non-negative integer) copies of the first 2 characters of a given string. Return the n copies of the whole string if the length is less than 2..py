# 23. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.

def calc(word, n):
    result = ""
    if len(word) > 2:
        for x in range(0, n):
            result += word[0: 2]
    else:
        # if its shorter than two = 1
        for x in range(0, n):
            result += word[0:1]

    print(result)


def main():
    calc("abcdef", 2)
    calc("p", 3)


if __name__ == "__main__":
    main()