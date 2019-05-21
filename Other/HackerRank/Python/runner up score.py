def minNumber(arr):
    number = arr[0]
    for x in arr:
        if number > int(x):
            number = x


    return number



def main():


    n = int(input())
    arr = (input())
    arr = arr.split(' ')

    if n < 2 or n > 10:
        print("there can be from 2 to 10 scores")
    else:
        largest = minNumber(arr)
        largest2 = largest

        for x in arr:
            if x > largest:
                largest2 = largest
                largest = x
            elif x < largest and x > largest2:
                largest2 = x

    print(str(largest2))

if __name__ == "__main__":
    main()