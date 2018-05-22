# Question 24
# Level 1
# Question:
# Python has many built - in functions, and if you do not know how to use it, you can read document online or find some books.
# But Python has a built- in document function for every built- in functions.
# Please write a program to print some Python built - in functions documents, such as abs(), int(), raw_input() And add document
# for your own function
# Hints:
# The built - in document method is __doc__
# TODO: print doc of custom function

def built_in_document_function(userInput):
    func = getattr(__builtins__, userInput)
    return (func.__doc__)


def main():
    while True:

        userInput = input("Enter python function or E[x]it: ")
        if userInput.upper() == "X":
            print("Good bye")
            break
        else:
            print(built_in_document_function(userInput))


if __name__ == "__main__":
    main()
