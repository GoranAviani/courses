#49. Write a Python program to convert list to list of dictionaries

#color_name = ["Black", "Red", "Maroon", "Yellow"]
#color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]
#[{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_nam
#e': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]

def fun (item1, item2):
    result = []
    for x in range(0, len(item1)):
        result.append({"color_name": item1[x], "color_code":item2[x]})
    return result


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun(["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]) == [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]


    print('Testing completed!')