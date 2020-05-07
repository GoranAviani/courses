#45. Write a python program to call an external command in Python.
from subprocess import call

def call_command():
    call(["ls", "-l"])

if __name__ == "__main__":
   call_command()