#11. Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array.
#The element value in the i-th row and j-th column of the array should be i*j.

#Test Data : Rows = 3, Columns = 4
#Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]


r = 3
c = 4
result = []
smallresult = []
##0 *1, 0 * 2
#1*1, 1*2

for x in range(r):
    smallresult = []
    for y in range(c):
        smallresult.append((x * y))

    result.append(smallresult)

print(result)
