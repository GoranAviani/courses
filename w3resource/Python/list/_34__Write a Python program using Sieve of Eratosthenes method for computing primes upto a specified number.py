# 34. Write a Python program using Sieve of Eratosthenes method for computing primes upto a specified number.


def fun(item1):
    # known way, neet to read about Sieve of Eratosthenes

    result = []
    for x in range(2, item1):
        isPrime = True
        for y in range(2, x):
            if x % y == 0:
                isPrime = False

        if isPrime == True:
            result.append(x)

    return result


if __name__ == "__main__":
    #  These "asserts" are used for self-checking and not for testing
    assert fun(6) == [2, 3, 5]
    assert fun(21) == [2, 3, 5, 7, 11, 13, 17, 19]

    print('Testing completed!')