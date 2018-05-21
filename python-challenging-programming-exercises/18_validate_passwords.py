# Question 18
# Level 3
# Question:
# A website requires the users to input username and password to register.
# Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.
# Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

def main():

    while True:
        userInput = input ("Enter passwords in list: ")

        if userInput == "X":
            print("Good bye!")
            break

        userInput = userInput.split(',')
        result = []

        for x in userInput:
            hasUpper, hasLower, hasNumber, hasSpecial = False,False,False,False

            if len(x) > 6 and len(x) < 12:
                for y in x:
                    if y.isalpha():
                        if y.isupper():
                            hasUpper = True
                        elif y.islower:
                            hasLower = True
                    elif y.isdigit():
                        hasNumber = True
                    elif y in ["*","'","-","_","#","@"]:
                        hasSpecial = True
                if (hasUpper and hasLower and hasNumber and hasSpecial) == True:
                    result.append(x)
        print("Valid passwords: " + str(result))
        print("As a string {}: ".format("".join(result)))

if __name__ == "__main__":
    main()
