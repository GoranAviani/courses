#3. Write a Python program to remove and print every
# third number from a list of numbers until the list becomes empty.

def print_every_third(numbers):
 counter = 0
 for number in numbers:
     counter += 1
     if counter % 3 == 0:
         print(number)

def main():
    user_input = input("Enter a list of numbers separated bu comma: ")
    user_input = user_input.split(',')
    print_every_third(user_input)


if __name__ == "__main__":
    main()




