#43. Write a Python program to split a list into different variables.

def fun(item1):
    var1, var2, var3 = item1
    return [var1, var2, var3]


if __name__ == "__main__":
    #  These "asserts" are used for self-checking and not for testing

    assert fun([("Black", "#000000", "rgb(0, 0, 0)"), ("Red", "#FF0000", "rgb(255, 0, 0)"),
             ("Yellow", "#FFFF00", "rgb(255, 255, 0)")]) == [("Black", "#000000", "rgb(0, 0, 0)"), ("Red", "#FF0000", "rgb(255, 0, 0)"),
             ("Yellow", "#FFFF00", "rgb(255, 255, 0)")]


    print('Testing completed!')