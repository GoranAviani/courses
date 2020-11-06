evens=[i**2 for i in range(10) if i**2 % 2 == 0]

print(evens)

a = [i for i in range(20) if i %3 == 0]
print(a)


#even = [2*i for i in range(10**100)]

# string formatting
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)