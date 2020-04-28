#21. Write a Python program to find whether a given number
# (accept from the user) is even or odd, print out an appropriate message
# to the user.

def start():
	user_input = input("Enter a number: ")
	try:
		number = int(user_input)
	except ValueError as e:
		print("{}" .format(e))
		quit()

	print("Number is even") if (number % 2 == 0) else print("Number is odd")

if __name__ == "__main__":
	start()