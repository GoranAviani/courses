#1
cat = True
dog = False
print(type(cat))

#2
print(cities)
first_alb = (cities[0] == 'Albuquerque')
print(first_alb)
second_alb = (cities[1] == 'Albuquerque')
first_last = (cities[0] == cities[-1])

#3
print(crime_rates)
first_500 = (crime_rates[0] > 500)
first_749 = (crime_rates[0] >= 749)
first_last = (crime_rates[0] >= crime_rates[-1])

#4
print(crime_rates)
second_500 = (crime_rates[1] < 500)
second_371 = (crime_rates[1] <= 371)
second_last = (crime_rates[1] <= crime_rates[-1])

result = 0
if cities[2] == 'Anchorage':
    result = 1


both_conditions = False
if crime_rates[0] > 500:
    if crime_rates[1] > 300:
        both_conditions = True


five_hundred_list = []

for cr in crime_rates:
    if cr > 500:
        five_hundred_list.append(cr)


print(crime_rates)
highest = 0
for x in crime_rates:
    if x > highest:
        highest = x
















