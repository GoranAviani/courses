#3. Write a Python function to multiply all the numbers in a list. Go to the editor
#Sample List : (8, 2, 3, -1, 7)
#Expected Output : -336


li = (8, 2 ,3, -1, 7)
res = 1

for number in li:
res *= number

print(str(res))
