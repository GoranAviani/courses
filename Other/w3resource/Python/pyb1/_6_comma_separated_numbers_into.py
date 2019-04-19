#6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. Go to the editor
#Sample data : 3, 5, 7, 23
#Output :
#List : ['3', ' 5', ' 7', ' 23']
#Tuple : ('3', ' 5', ' 7', ' 23')


userInput = "3, 5, 7, 23"
listUserInput = userInput.split(", ")
resultList = []
resultTuple = ()

for x in listUserInput:
   # print(x)
    resultList.append(x)
    resultTuple += (x,)

   # print(type(resultList))
   # print(type(resultTuple))

for x in resultList:
   print(x)

for z in resultTuple:
    print(z)