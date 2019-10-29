#21. Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.

def start():
	userInput = int(input("enter a num"))
	if (userInput % 2 == 0):
		print("num is even")
	else:
		print("num is odd")

if __name__ == "__main__":
	start()