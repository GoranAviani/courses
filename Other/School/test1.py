

#print(list(range(2)) + list('abc'))

#userInput = "3 4 5 10 50"
#for x in userInput.split():
#    print(x)

#list1 = [6,7,8,9,10]
#print(list1[1:3])

list1 = [6, 7, 8, 9, 10]

list1[0] = 20
#20,7,8,9,10
del list1[1]
#20,8,9,10
del list1[1]
#20,9,10
list1[1] = 30
#20,30,10
list1.append(40)
#20,30,10,40


print(list1)