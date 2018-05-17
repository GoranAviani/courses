import datetime

def print_header():
    print('-----------------------------')
    print('     BIRTHDAY APP')
    print('-----------------------------')

def get_birthday_from_user():
    print("when were you born?")
    year = int(input("Year YYYY: "))
    month = int(input("Month MM: "))
    day = int(input("Day DD: "))

    birthDay = datetime.date(year, month, day)
    return birthDay


def compute_days_between_dates(bdayDate, nowDate):
    thisYear = datetime.date(year=nowDate.year, month=bdayDate.month, day=bdayDate.day)

    dt = thisYear - nowDate
    return dt.days

def print_birthday_information(days):
    if days <0:
        print("You had your birthday {0} days ago this year" .format(-days))
    elif days >0:
        print("You birthday is in {0} days" .format(days))
    else:
        ("Today is your birthday")

def main():
    print_header()
    bday = get_birthday_from_user()
    print(bday)
    now = datetime.date.today()
    print(now)
    numberOfDays = compute_days_between_dates(bday,now)
    print_birthday_information(numberOfDays)

main()