#Fibonacci numbers:

#1,1,2,3,5,8,13,21...

def fibonacci(limit):
    numbers = []
    current = 0
    next = 1
    while current < limit:
        #current, next = next, next + current

        current_old = current
        current = next
        next = current_old + next
        numbers.append(current)

    return numbers

print(fibonacci(100))