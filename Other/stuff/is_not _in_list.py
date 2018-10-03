
alls = [numbers1]
dontwant = [numbers_we_dont_want_in_new_list]

result = []

for x in alls:
    if x not in dontwant:
        result.append(x)

# print(result)
for y in result:
    print(y)