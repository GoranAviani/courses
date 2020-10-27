number_list=list(range(1,51))
print(number_list)

divided_by_7=[number for number in number_list if number % 7 == 0]

odd_new=[]
even_new=[]
for number in number_list:
    if number % 2 == 1:
        if number % 7 != 0:
            odd_new.append(number)

    if number % 2 == 0:
        if number % 7 != 0:
            even_new.append(number)

print(odd_new)
print(even_new)
print(divided_by_7)

### Ovo mozes rjesit jos ovako:
odd_new1 = []
even_new1 = []
divided_by_71 = []

for number1 in number_list:
    if number1 % 7 == 0:
        divided_by_71.append(number1)
    elif number1 % 2 == 0:
        even_new1.append(number1)
    else:
        odd_new1.append(number1)

print("lista odd: {}" .format(odd_new1))
print("lista even: {}" .format(even_new))
print("lista divided by 7: {}" .format(divided_by_71))
