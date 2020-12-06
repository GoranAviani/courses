#Riješite i predajte rješenje za zadatak:
#Mata uzgaja i prodaje lubenice. Za svaku lubenicu manju od 5 kg može dobiti 1,5 kn za kilogram, dok za teže lubenice dobije 3 kn po kilogramu.
# Napišite program u Pythonu koji će omogućiti unos težine n lubenica te izračunati ukupan iznos u kunama koji Mata može dobiti za sve te lubenice.
#Napomena: Koristite naredbu za ponavljanje while i unos lubenica sve dok se ne unese 0.

izracun = 0
while True:
    x = input("")
    x = float(x)
    if x == 0.0:
        break
    elif x < 5:
        izracun = izracun + (x * 1.5)

    elif x >= 5:
        izracun = izracun + (x * 3)
print("{}".format(izracun))