
alls = [1","2","3"]
dontwant = [1","2"]
            
result = []

for x in alls:
    if x not in dontwant:
        result.append(x)

# print(result)
for y in result:
    print(y)
