#igrac1= "tuljan foka lav tigar auto zica li op pp ii"
#igrac2 = "foka macka pas tuljan tica zica lala ppppp"

igrac1 = input("")
igrac2 = input("")

igrac1 = set(igrac1.split(" "))
igrac2 = set(igrac2.split(" "))

bodovi1 = 0
bodovi2 = 0

for x in igrac1:
    if x not in igrac2:
        bodovi1 +=1

for y in igrac2:
    if y not in igrac1:
        bodovi2 += 1


if bodovi1 > bodovi2:
    print("Marica")
elif bodovi2 > bodovi1:
    print("Ivica")
else:
    print("neriješeno")
