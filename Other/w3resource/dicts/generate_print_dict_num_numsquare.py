#6.Write a Python script to generate and print a dictionary that contains a number
# (between 1 and n) in the form (x, x*x). Go to the editor
#Sample Dictionary ( n = 5) :
#Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}



userInput = 5
result = {}

for x in range(1, userInput+1):
    result[x] = x * x

print(result)