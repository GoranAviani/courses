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


def fibonacci2(limit):
    numbers = []
    current = 0
    next = 1
    while current < limit:
        #current, next = next, next + current

        current_old = current
        current = next
        next = current_old + next
        numbers.append(current)
        yield current


for x in fibonacci2(150):
    print(x, end=", ")


print("\n")
def fibonacci2(limit):
    numbers = []
    current = 0
    next = 1
    while True:
        #current, next = next, next + current

        current_old = current
        current = next
        next = current_old + next
        numbers.append(current)
        yield current


for x in fibonacci2(150):
    if x > 1000:
        break
    print(x, end=", ")