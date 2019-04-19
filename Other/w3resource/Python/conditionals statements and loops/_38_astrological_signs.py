#8. Write a Python program to display astrological sign for given date of birth. Go to the editor
#Expected Output:

#Input birthday: 15
#Input month of birth (e.g. march, july etc): may
#Your Astrological sign is : Taurus



uiDay = int(input("Input birthday: "))
uiMonth = input("Input month of birth (e.g. march, july etc): ")
uiMonth = uiMonth.lower()
uiDay = int(uiDay)
if uiMonth == 'december':
    astroSign = 'Sagittarius' if (uiDay < 22) else 'capricorn'
elif uiMonth == 'january':
    astroSign = 'Capricorn' if (uiDay < 20) else 'aquarius'
elif uiMonth == 'february':
    astroSign = 'Aquarius' if (uiDay < 19) else 'pisces'
elif uiMonth == 'march':
    astroSign = 'Pisces' if (uiDay < 21) else 'aries'
elif uiMonth == 'april':
    astroSign = 'Aries' if (uiDay < 20) else 'taurus'
elif uiMonth == 'may':
    astroSign = 'Taurus' if (uiDay < 21) else 'gemini'
elif uiMonth == 'june':
    astroSign = 'Gemini' if (uiDay < 21) else 'cancer'
elif uiMonth == 'july':
    astroSign = 'Cancer' if (uiDay < 23) else 'leo'
elif uiMonth == 'august':
    astroSign = 'Leo' if (uiDay < 23) else 'virgo'
elif uiMonth == 'september':
    astroSign = 'Virgo' if (uiDay < 23) else 'libra'
elif uiMonth == 'october':
    astroSign = 'Libra' if (uiDay < 23) else 'scorpio'
elif uiMonth == 'november':
	astroSign = 'scorpio' if (uiDay < 22) else 'sagittarius'
print("Your Astrological sign is :  {}".format(astroSign))