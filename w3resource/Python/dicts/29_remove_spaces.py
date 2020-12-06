#29. Write a Python program to remove spaces from dictionary keys.


student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
result = {}
for k , v in student_list.items():
    if " " in k:
        k = k.replace(" ", "")
        print(k)
        result[k] = v

print(student_list)
print(result)