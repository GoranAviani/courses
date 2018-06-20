File = open('dq_unisex_names.csv', 'r')
names = File.read()


f = open('dq_unisex_names.csv', 'r')
names = f.read()

names_list = names.split('\n')
first_five = names_list[0:5]
print(first_five)




f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split('\n')

nested_list = []
comma_list = []
for x in names_list:
    print(x.split(','))
    comma_list.append(x.split(','))

for y in comma_list:
    nested_list.append(y)
    
print(nested_list[0:5])









