#Question:
#Define a function that can accept two strings as input and print the string with maximum length
#in console. If two strings have the same length, then the function should print al l strings line by line.
#Hints:
#Use len() function to get the length of a string

def string_length(str1,str2):
    if len(str1)>len(str2):
        print(str1)
    elif len(str1)<len(str2):
        print(str2)
    else:
        print(str1+"\n"+str2)

string_length("1","ab")

