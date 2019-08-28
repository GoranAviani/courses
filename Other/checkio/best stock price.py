# You are given the current stock prices. You have to find out which stocks cost more.
#Input: The dictionary where the market identifier code is a key and the value is a stock price.
#Output: A string and the market identifier code.
#Preconditions: All the prices are unique.



def best_stock(data):
    # your code here
    #print(data)
    resKey = list(data.keys())[0]
    resNum = list(data.values())[0]

    #print(resKey)
    #print(resNum)
    counter = 0
    for k, v in data.items():
        if resNum < v:
            resKey = k
            resNum = v
        counter += 1


    counterText = ""
    if counter == 0:
        counterText = "First"
    elif counter == 1:
        counterText = "Second"
    elif counter == 2:
        counterText = "Third"
    return resKey#, counterText



if __name__ == '__main__':
    print("Example:")
    print(best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }) == 'ATX', "First"
    assert best_stock({
        'CAC': 91.1,
        'ATX': 1.01,
        'TASI': 120.9
    }) == 'TASI', "Second"
    print("Coding complete? Click 'Check' to earn cool rewards!")
