# Find all nums from 1000 to 3500 whih are divisable only by 7 and 5.
"""
for x in range(1000, 3501):
    if ((x % 7 == 0) and (x % 5 == 0)):
        print("{}".format(x))
"""

result = []
for x in range( 1000, 3501):
    if ((x % 7 == 0) and (x % 5 == 0)):
        result.append(x)


#for x in result:
#    print("{}".format(x))





def nums(result):
    print('Starting')
    for y in result:
        print (y)




nums(result)


