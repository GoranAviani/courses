#24. Write a Python program to test whether a passed letter is a vowel or not


def check_vowel(x):
	if x in ["a", "e", "i", "o","u"]:
		return ("Vowel")
	else:
		return("Not vowel")

def main():
	userInput = input("Enter a letter: \n")
	result = check_vowel(userInput)
	print(result)

if __name__ == "__main__":
	main()