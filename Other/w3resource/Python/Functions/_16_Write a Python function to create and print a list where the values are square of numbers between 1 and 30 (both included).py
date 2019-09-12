#16. Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included).



def fun():
    result=[]
    for x in range(1,31):
        result.append(x**2)

    print(result)
    return result



if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for testing
    assert fun() == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900]

    print('Testing completed!')