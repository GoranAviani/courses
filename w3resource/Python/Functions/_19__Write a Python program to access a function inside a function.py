#19. Write a Python program to access a function inside a function.


def fun(item1):
        def sum_all(item2):
            return item1 + item2
        return sum_all

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun(5)(10) == 15

    print('Testing completed!')