#40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
def fun(item1, item2):
    import math
    dist = math.sqrt((item1[1] - item1[0])**2 + (item2[1] - item2[0])**2)
    dist = round(dist, 2)
    return dist

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun([4, 0], [6, 0]) == 7.21

    print('Testing completed!')