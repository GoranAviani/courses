def fun (list):
    result =[]
    for x in list:
       if x not in result:
           result.append(x)

    return result


if __name__ == '__main__':

    assert fun(["k","u","c","a"]) == ["k","u","c","a"]
    assert fun(["T","o"]) == ["T","o"]
    assert fun([1,2,3,1,2,3]) == [1,2,3]


    print("Coding complete!")