#V = 4/3 × π × r3 = π × d3/6.
result = 0
userInput = abs(float(input("Enter a number: \n")))
if userInput < 17:
	result = 17 - userInput
	print(str(result))
elif userInput > 17:
	result = (17 - userInput) * 2
	print(str(result))
else:
	print(" Number is 17.  Input lower or greatver num than 17")