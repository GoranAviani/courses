#43. Write a Python program to get OS name, platform and release information.
import os

def get_os_info():
    return os.uname()

if __name__ == "__main__":
    result = get_os_info()
    print(result)