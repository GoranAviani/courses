#47. Write a Python program to lowercase first n characters in a string.


def fun(text, number):
    result = []
    counter = 0
    for x in text:
        if counter < number:
            counter += 1
            result.append(x.lower())
        else:
            result.append(text[6 : len(text)])
            result = "".join(result)
            print(result)
            return result

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("kUCa MAMA auto", 6) =="kuca mAMA auto"

    print('Testing completed!')