"""
 You are at the beginning of a password series. Every mission is based on the previous one.
 Going forward the missions will become slightly more complex.
In this mission, you need to create a password verification function.
The verification condition is:
    the length should be bigger than 6.
"""

def main(password = "muchlonger5"):
    digs = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    has_d_in_password = False

    for d in digs:
        if d in password:
            has_d_in_password = True
            break

    if has_d_in_password == True:
        if len(password) > 6:
            return True
        else:
            return False

    return False

if __name__ == '__main__':
    main()