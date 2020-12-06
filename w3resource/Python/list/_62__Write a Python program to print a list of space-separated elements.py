#_62__Write a Python program to print a list of space-separated elements

def fun(item1):
#    result = ""
#    for x in range(0, len(item1)):
#       if x == len(item1)-1:
#            result += str(item1[x])
#       else:
#            result += str(item1[x]) + " "

#    return result

    return " ".join(item1)

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun(["a", "b", "5", "7", "a"]) == "a b 5 7 a"


    print('Testing completed!')