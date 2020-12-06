# You have a table with all available goods in the store. The data is represented as a list of dicts
#Your mission here is to find the TOP most expensive goods. The amount we are looking for will be given as a first argument and the whole data as the second one
#Input: int and list of dicts. Each dicts has two keys "name" and "price"
#Output: the same as the second Input argument.



def bigger_price(limit: int, data: list) -> list:
    """
        TOP most expensive goods
    """
    # your code here


    topName = data[0]["name"]
    topPrice = data[0]["price"]
    secondName = ""
    secondPrice = 0

    for x in data:
        if x["price"] > topPrice:
            topPrice = x["price"]
            topName = x["name"]

    if limit == 2:
        for x in data:
            if  x["price"] < topPrice and x["price"] > secondPrice:
                secondPrice = x["price"]
                secondName = x["name"]

    result = [{"name": topName, "price": topPrice}]
    if limit == 2:
        result.append({"name": secondName, "price": secondPrice})

    return result


if __name__ == '__main__':
    from pprint import pprint
    print('Example:')
    pprint(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))

    # These "asserts" using for self-checking and not for auto-testing
    assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
        {"name": "wine", "price": 138},
        {"name": "bread", "price": 100}
    ], "First"

    assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}], "Second"

    print('Done! Looks like it is fine. Go and check it')
