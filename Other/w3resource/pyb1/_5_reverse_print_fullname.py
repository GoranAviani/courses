#5. Write a Python program which accepts the user's first and last name and print them in reverse
# order with a space between them.


def revNames(first, last):

    return ("{} {}".format(first[::-1], last[::-1]))


result = revNames("Goran", "Aviani")

print(result)