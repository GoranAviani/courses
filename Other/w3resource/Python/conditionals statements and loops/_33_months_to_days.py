

#33. Write a Python program to convert month name to a number of days. Go to the editor
#Expected Output:
# List of months: January, February, March, April, May, June, July, August
#, September, October, November, December
#Input the name of Month: February
#No. of days: 28/29 days

ui = input (" input month")

if ui == "February":
print("No. of days: 28/29 days")
elif ui in ("April", "June", "September", "November"):
print("No. of days: 30 days")
elif ui in ("January", "March", "May", "July", "August", "October", "December"):
print("No. of days: 31 day")
else:
print("Wrong month name")
