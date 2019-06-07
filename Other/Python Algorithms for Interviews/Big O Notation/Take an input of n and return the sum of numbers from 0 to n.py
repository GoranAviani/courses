'''
Take an input of n and return the sum of numbers from 0 to n
'''




def sum_of_numbers(n):
    sumOfNum = 0
    for x in range(0, n+1):
        sumOfNum += x
    print(sumOfNum)

sum_of_numbers(5)


def sum_of_numbers2(n):
    print(str((n*(n+1))/2))

sum_of_numbers2(5)