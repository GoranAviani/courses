#43. Write a Python program to get OS name, platform and release information.

def fun():
    import os
    os_info = os.uname()
    return (os_info)

if __name__ == "__main__":
    result = fun()
    print(result)