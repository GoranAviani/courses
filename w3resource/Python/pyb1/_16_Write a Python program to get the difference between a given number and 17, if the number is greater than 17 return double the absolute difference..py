#V = 4/3 × π × r3 = π × d3/6.
result = 0
userInput = abs(float(input("Enter a number: \n")))
if userInput == 17:
	result = (" Number is 17.  Input lower or greatver num than 17")
elif userInput < 17:
	result = 17 - userInput
elif userInput > 17:
	result = (17 - userInput) * 2
print(str(result))
