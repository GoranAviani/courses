#40. Write a Python program to reverse words in a string.

def fun(text):
    text = text.split(" ")
    result = []
    result1 = ""
    for x in range(len(text)-1, -1, -1):
        result.append(text[x])

    result = " ".join(result)
    return result

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("kuca auto") == "auto kuca"
    assert fun("Write a Python program to reverse words in a string") == 'string a in words reverse to program Python a Write'


    print('Testing completed!')