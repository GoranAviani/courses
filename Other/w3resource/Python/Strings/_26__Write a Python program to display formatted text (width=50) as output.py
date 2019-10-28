#26. Write a Python program to display formatted text (width=50) as output.


def fun(text):
    result =""
    counter = 0
    for x in text:
         counter +=1
         result += x
         if counter == 49:# because char 50 should be -
            counter = 0
            if x.isalpha():
                result = result + ("-/n")
            else:
                result = result + ("/n")

    print(result)
    return result


if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for testing
    assert fun("po sumama i gorama.po sumama i gorama.po sumama i gorama.") == "po sumama i gorama.po sumama i gorama.po sumama i-/n gorama."


    print('Testing completed!')