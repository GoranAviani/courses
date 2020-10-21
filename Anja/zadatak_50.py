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