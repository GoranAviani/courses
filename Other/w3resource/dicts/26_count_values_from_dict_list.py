

#26. Write a Python program to count the values associated with key in a dictionary. Go to the editor
#Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
#Expected result: Count of how many dictionaries have success as True

userInput = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]

result =0
for x in userInput:
    if x["success"]:
        result +=1
print("{}".format(result))
