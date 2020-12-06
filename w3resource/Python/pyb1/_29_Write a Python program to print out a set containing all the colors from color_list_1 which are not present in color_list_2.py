# 29. Write a Python program to print out a set containing
# all the colors from color_list_1 which are not present in color_list_2.
'''
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :
{'Black', 'White'}
'''

def main():
    color_list_1 = ["White", "Black", "Red"]
    color_list_2 = ["Red", "Green"]
    result = []

    for x in color_list_1:
        if x not in color_list_2:
            result.append(x)
    print(set(result))

if __name__ == "__main__":
    main()
