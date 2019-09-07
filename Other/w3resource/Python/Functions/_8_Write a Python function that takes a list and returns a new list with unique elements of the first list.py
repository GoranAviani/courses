def fun (list):
    result =[]
    for x in list:
       if x not in result:
           result.append(x)
    
    return result