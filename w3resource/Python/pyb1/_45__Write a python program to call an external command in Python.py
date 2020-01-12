#45. Write a python program to call an external command in Python.

def fun():
    from subprocess import call
    call(["ls", "-l"])

if __name__ == "__main__":
   fun()