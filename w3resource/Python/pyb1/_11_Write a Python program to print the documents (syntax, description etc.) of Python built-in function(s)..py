'''
11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument.
'''

print(abs.__doc__)
userInfo = float(input("enter a int or float: \n"))
print(str(abs(userInfo)))

