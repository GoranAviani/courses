#23. Write a Python program to combine values in python list of dictionaries. Go to the editor
#Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
#Expected Output: Counter({'item1': 1150, 'item2': 300})

data =  [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

result = []
itemsinresult = []

for x in data:
   print(x)
   # print(x['item'])
#   print(x['amount'])
   newdict = {}
   if x['item'] not in itemsinresult:   
      newdict[x['item']] = x['amount']
      itemsinresult.append(x['item'])
      result.append(newdict)
   else:
      for z in result:
          if x['item'] in z:
              z[x['item']] += x['amount']     
            
     
       
            
print(result)
