#4. Write a Python program to construct the following pattern, using a nested for loop.
#*
#* *
#* * *
#* * * *
#* * * * *
#* * * *
#* * *
#* *
#*

counter = 1
for x in range(5):
    for y in range(x):
        print("*",end="")
    print("")

for x in range(5,0,-1):
    for y in range(x):
        print("*",end="")
    print("")
