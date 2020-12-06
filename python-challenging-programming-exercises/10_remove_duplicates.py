# Question 10
# Level 2
# Question:
# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing
# all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# We use set container to remove duplicated data automatically and then use sorted() to sort the data.

def remove_duplicates(text):
    text = sorted(set(text))
    return (' '.join(text))

def main():
    while True:
        userInput = input("Enter sentence or E[x]it: ").split()
        if userInput[0].upper() == "X":
            print("Good bye!")
            break
        print(remove_duplicates(userInput))

if __name__ == "__main__":
    main()
