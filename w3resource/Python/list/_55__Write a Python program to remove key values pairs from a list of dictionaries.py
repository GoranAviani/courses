#55. Write a Python program to remove key values pairs from a list of dictionaries.


def fun(item1, item2):
   result = []
   for x in item1:
       for k, v in x.items():
           if k == item2:
               pass
           else:
               result.append({k:v})
   return result

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun([{'key1':'value1', 'key2':'value2'}, {'key1':'value3', 'key2':'value4'}] , "key1") == [{'key2': 'value2'}, {'key2': 'value4'}]


    print('Testing completed!')