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
"""
def nums(result):
    print('Starting')
    for y in result:
        print (y)

nums(result)
"""

###################

#Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each other.


##write a py fun that takes a sequence of nums and shows dupllicate. show only one duplciate.
def unique(nums):
    result = []
    nums = sorted(nums)
    for x in nums:
        if nums.count(x) > 1 and x not in result:
            result.append(x)
    for y in result:
        print(y)


nums = [1,8,3,8,4,5,6,7,8,1,4,2,5,5,3]
unique(nums)