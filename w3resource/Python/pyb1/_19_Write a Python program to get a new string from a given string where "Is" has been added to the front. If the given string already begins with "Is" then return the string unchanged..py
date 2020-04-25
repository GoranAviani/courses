#19. Write a Python program to get a new string from a given string where "Is"
# has been added to the front. If the given string already begins with "Is"
# then return the string unchanged.


def main():
	userInput = input("Enter a string: \n")
	print(userInput) if userInput[0:2] == "Is" else print("Is" + userInput)

if __name__ == "__main__":
	main()