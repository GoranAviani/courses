'''

12. Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.
'''

import calendar

def main():
    userMonth = int(input("Input month: "))
    userYear = int(input("Input year: "))

    print(calendar.month(userYear, userMonth))

if __name__ == "__main__":
    main()
