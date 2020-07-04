# Python module to execute
import file_two

print("File one __name__ is set to: {}" .format(__name__))

def function_one():
    print("Function one is executed")


if __name__ == "__main__":
    print("Executed when invoked directly")
    file_two.function_two()
else:
    print("Executed when imported")
