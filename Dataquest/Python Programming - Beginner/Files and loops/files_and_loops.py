f = open("crime_rates.csv", "r")
print(f)


f = open("crime_rates.csv", "r")
data = f.read()



# We can split a string into a list.
sample = "john,plastic,joe"
split_list = sample.split(",")
print(split_list)

# Here's another example.
string_two = "How much wood\ncan a woodchuck chuck\nif a woodchuck\ncould chuck wood?"
split_string_two = string_two.split('\n')
print(split_string_two)

# Code from previous cells
f = open('crime_rates.csv', 'r')

data = f.read()


f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split("\n")
print(rows)




ten_rows = rows[0:10:1]
for ten_row in ten_rows:
    print(ten_row)



three_rows = ["Albuquerque,749", "Anaheim,371", "Anchorage,828"]
final_list = []
for row in three_rows:
    split_list = row.split(',')
    final_list.append(split_list)
print(final_list)
print(final_list[0])
print(final_list[1])
print(final_list[2])




f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows[0:5])
final_data = []
for x in rows:
    final_data.append(x.split(","))
    print(final_data)




print(five_elements)
cities_list=[]

for x in five_elements:
    cities_list.append(x[0])




crime_rates = []
cities_list = []

for row in five_elements:
    # row is a list variable, not a string.
    crime_rate = row[1]

    # crime_rate is a string, the crime rate of the city.
    crime_rates.append(crime_rate)
    
    
cities_list = []
for x in final_data:
    cities_list.append(x[0])









