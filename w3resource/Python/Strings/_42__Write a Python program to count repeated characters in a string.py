#42. Write a Python program to count repeated characters in a string.


def fun(text):
    letters = {}
    result = []
    for x in text:
        #We dont want to count empty spaces
        if x == " ":
            continue

        if x in letters:
            letters[x] += 1
        else:
            letters[x] = 1

    for k, v in letters.items():
        if v > 1:
            result.append(str(k)+"="+str(v))

    result = ",".join(result)
    return result

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("kuca mama auto") == "u=2,a=4,m=2"
    assert fun("thequickbrownfoxjumpsoverthelazydog") == "t=2,h=2,e=3,u=2,r=2,o=4"


    print('Testing completed!')