# Question 17
# Level 2
# Question:
# Write a program that computes the net amount of a bank account based a transaction log from console input. T
# he transaction log format is shown as following:
# D 100
# W 200
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

def main():
    userInput=None
    numbers={'Deposit':0, 'Withdrawal':0}
    while userInput != "X":
        userInput = input("[D]eposit\n[W]ithdrawal\n[L] for [List] current stock\n[x] for E[x]it: ")
        userInput=userInput.upper()
        if userInput[:1]=="D":
            numbers['Deposit']+=int(userInput[2:])
        elif userInput[:1]=="W":
            numbers['Withdrawal']+=int(userInput[2:])
        elif userInput[:1]=="X":
            print("BYE! \n Sum of the stock is {}".format(numbers['Deposit']-numbers['Withdrawal']))
        elif userInput[:1]=="L":
            print("Current sum of the stock is: {}".format(numbers['Deposit']-numbers['Withdrawal']))
        else:
            print("Please try again. I don't understand")
            
if __name__ == "__main__":
    main()
