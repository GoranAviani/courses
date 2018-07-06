#Writing Files


#When a file is opened in write mode, the file's existing content is deleted.
file = open("newfile.txt", "r")
print("Reading initial contents")
print(file.read())
print("Finished")
file.close()

file = open("newfile.txt", "w")
file.write("Some new text")
file.close()

file = open("newfile.txt", "r")
print("Reading new contents")
print(file.read())
print("Finished")
file.close()


##Result: >>>
#Reading initial contents
#some initial text
#Finished
#Reading new contents
#Some new text
#Finished
#>>>



#The write method returns the number of bytes written to a file, if successful.
msg = "Hello world!"
file = open("newfile.txt", "w")
amount_written = file.write(msg)
print(amount_written)
file.close()

Result: >>>
12
>>>

If a file write operation is successful, which one of these statements will be true?
file.write(msg) == len(msg)


#Working with Files
#It is good practice to avoid wasting resources by making sure that files are always closed after they have been used. One way of doing this is to use try and finally.try:
   f = open("filename.txt")
   print(f.read())
finally:
   f.close()


#Working with Files

#An alternative way of doing this is using with statements. This creates a temporary variable (often called f), which is only accessible in the indented block of the with statement. with open("filename.txt") as f:
#   print(f.read())
#The file is automatically closed at the end of the with statement, even if exceptions occur within it.




Dictionaries
#Only immutable objects can be used as keys to dictionaries. Immutable objects are those that can't be changed. So far, the only mutable objects you've come across are lists and dictionaries. Trying to use a mutable object as a dictionary key causes a TypeError.


bad_dict = {
  [1, 2, 3]: "one two three", 
}
#Result: >>>
#TypeError: unhashable type: 'list'
#>>>












nums = {
  1: "one",
  2: "two",
  3: "three",
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)



















