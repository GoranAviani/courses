# Write a Python program to count the number of even and odd numbers from a series of numbers. Go to the editor
#Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

nums = "1, 2, 3, 4, 5, 6, 7, 8, 9"

nums = nums.split(", ")
even = 0
odd = 0

for x in nums:
    if float(x) % 2 == 0:
        even += 1
    else:
        odd += 1

print("{} {} ".format(even, odd))