#37. Write a Python program that reads two integers representing a month and day and prints the season for that month and day. Go to the editor
#Expected Output:

#Input the month (e.g. January, February etc.): july
#Input the day: 31
#Season is autumn

uiMonth = input("Enter month: ")
uiDay = int(input("Enter day: "))



if uiMonth.lower() in ('january', 'february', 'march'):
	season = 'winter'
elif uiMonth.lower() in ('april', 'aay', 'june'):
	season = 'spring'
elif uiMonth.lower() in ('july', 'august', 'september'):
	season = 'summer'
else:
	season = 'autumn'


if (uiMonth.lower == 'march') and (uiDay > 19):
	season = 'spring'
elif (uiMonth == 'june') and (uiDay > 20):
	season = 'summer'
elif (uiMonth == 'september') and (uiDay > 21):
	season = 'autumn'
elif (uiMonth == 'december') and (uiDay > 20):
	season = 'winter'

print("Season is {}".format(season))