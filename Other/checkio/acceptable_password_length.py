"""
 You are at the beginning of a password series. Every mission is based on the previous one.
 Going forward the missions will become slightly more complex.
In this mission, you need to create a password verification function.
The verification condition is:
    the length should be bigger than 6.
"""

def main(password):
    if len(password) > 6:
        return True
    else:
        return False

if __name__ == '__main__':
    main()