

brojevi = input("")
#brojevi = "130 78 90 123 75 98 83 101 99 94 78"
#brojevi = "100 200 300 400 500"

brojevi = brojevi.split()
najveci1 = 0
najveci2 = 0
najveci3 = 0

for x in brojevi:

    if int(x) > int(najveci2):
        najveci3 = najveci2
        najveci2 = x
    if int(x) > int(najveci1):
        najveci2 = najveci1
        najveci1 = x


for y in brojevi:
    if int(y) > int(najveci3) and y < najveci2:
        najveci3 = y


print(najveci1)
print(najveci2)
print(najveci3)
