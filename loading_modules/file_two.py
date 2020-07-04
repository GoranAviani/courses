# Python module to import

print("File two __name__ is set to: {}" .format(__name__))

def function_two():
    print("Function two is executed")

def function_three():
    print("Function three is executed")

if __name__ == "__main__":
    print("File two executed when invoked directly")
else:
    print("File two executed when imported")