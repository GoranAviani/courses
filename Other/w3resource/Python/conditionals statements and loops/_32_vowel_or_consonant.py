

#32. Write a Python program to check whether an alphabet is a vowel or consonant. Go to the editor
#Expected Output:

#Input a letter of the alphabet: k
#k is a consonant.
wovels=["a","e","i","o","u"]
while True:
userInput = input("please enter a letter : ")
if userInput.upper() == "EXIT":
print("Good bye")
break

if userInput in wovels:
print("its a vowel")
else:
print("its ok")
