#9. Write a Python program to get the Fibonacci series between 0 to 50.
#Every next number is found by adding up the two numbers before it.


num1 = 0
num2 = 1
res = 0

while res < 50:
    res = num1 + num2
    print(res)
    num1 = num2
    num2 = res