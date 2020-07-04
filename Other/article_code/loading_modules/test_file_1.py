# Suppose this is foo.py.
import test_file_2

print("before import")
import math

print("before functionA")
def functionA():
    print("Function A")

print("before __name__ guard")
if __name__ == '__main__':
    functionA()

print("after __name__ guard")