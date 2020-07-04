# Python program to execute
# main directly
print("Always executed")


def function_one():
    print("Function one is executed")

print("File one __name__ is set to: {}" .format(__name__))
if __name__ == "__main__":
    print("Executed when invoked directly")
else:
    print("Executed when imported")
