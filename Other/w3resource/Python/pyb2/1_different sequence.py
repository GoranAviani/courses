#Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each other.

def diffNums(seq):
    if len(seq) == len(set(seq)):
        return ("It's OK")
    else:
        return ("Not OK")


OKseq = [1,2,3,5,7]
NotOKseq = [1,1,3,4,5]

print(diffNums(OKseq))
print(diffNums(NotOKseq))

"""
##my idea: write a py fun that takes a sequence of nums and shows dupllicate. show only one number of each duplciate.
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

"""