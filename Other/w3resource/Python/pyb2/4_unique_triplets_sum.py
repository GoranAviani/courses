#4. Write a Python program to find unique triplets whose three elements gives the sum of zero from an array of n integers.


#testing

def triplets(userInput):
       for x in userInput:
           print("prvi {} ".format(x))
           for y in userInput:
              print("drugi {} ".format(y))
              for z in userInput:
                  print("treci {} ".format(y))





userInput = [1,2,-2,4,-6, 3]
triplets(userInput)