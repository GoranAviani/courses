#40. Write a Python program to compute the distance between the
# points (x1, y1) and (x2, y2).
import math

def calculation(**kwargs):
    try:
        item1 = kwargs["item1"]
        item2 = kwargs["item2"]
    except KeyError as e:
        print("Can not fetch variable {}" .format(e))
    else:
        dist = math.sqrt((item1[1] - item1[0])**2 + (item2[1] - item2[0])**2)
        dist = round(dist, 2)
        return dist

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    all_items = {"item1": [4, 0], "item2": [6, 0]}
    assert calculation(**all_items) == 7.21
    print('Testing completed!')