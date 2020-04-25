#22. Write a Python program to count the number 4 in a given list

def start():
	result = 0
	given_list = [1, 2, 4, 6, 4, 8, 4]
	for number in given_list:
		if number ==4:
			result +=1
	print("There are {} number fours." .format(result))

if __name__ == "__main__":
	start()