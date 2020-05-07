#4. Write a Python program to find unique triplets whose
# three elements gives the sum of zero from an array of n integers.

def triplets(userInput):
    result = []
    for x in userInput:
       for y in userInput:
          for z in userInput:
              if x + y + z == 0:
                  result.append("{},{},{}" .format(x,y,z))

    print(result)



userInput = [1,2,-2,4,-6, 3]
triplets(userInput)