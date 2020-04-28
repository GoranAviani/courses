# 23. Write a Python program to get the n (non-negative integer)
# copies of the first 2 characters of a given string.
# Return the n copies of the whole string if the length is less than 2.

def calc(word, n):
    result = ""
    try:
        word = str(word)
        n = int(n)
    except ValueError as e:
        print("{}" .format(e))
        quit()

    word_length = len(word)
    if word_length > 2:
        for x in range(0, n):
            result += word[0: 2]
    elif word_length == 1:
        for x in range(0, n):
            result += word
    else:
        result = "Please input positive number"
    print(result)


def main():
    calc("abcdef", "2")
    calc(2, 3)


if __name__ == "__main__":
    main()