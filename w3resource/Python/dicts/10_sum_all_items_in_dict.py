#10. Write a Python program to sum all the items in a dictionary.

my_dict = {'data1':100,'data2':-54,'data3':247}
result = 0

for k, v in my_dict.items():
    result += v

print(str(result))
