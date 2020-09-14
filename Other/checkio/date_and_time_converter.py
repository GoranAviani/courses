'''
Computer date and time format consists only of numbers, for example: 21.05.2018 16:30
Humans prefer to see something like this: 21 May 2018 year, 16 hours 30 minutes
Your task is simple - convert the input date and time from computer format into a "human" format.

example

Input: Date and time as a string

Output: The same date and time, but in a more readable format

Example:
date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
date_time("19.09.2999 01:59") == "19 September 2999 year 1 hour 59 minutes"
date_time("21.10.1999 18:01") == "21 October 1999 year 18 hours 1 minute"
# NB: words "hour" and "minute" are used only when time is 01:mm (1 hour) or hh:01 (1 minute).
# In other cases it should be used "hours" and "minutes".
'''

MONTH_NUMBER = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May',
                '6': 'June', '7': 'July', '8': 'August', '9': 'September', '10': 'October',
                '11': 'November', '12': 'December'}

def remove_leading_zero(text: str):
    if text[:1] == '0':
        return text[1:]
    return text


def date_time(date_and_time: str) -> str:
    date_and_time_list = date_and_time.split(' ')
    date = date_and_time_list[0]
    time = date_and_time_list[1]

    date = date.split('.')
    time = time.split(':')

    day = date[0]
    day = remove_leading_zero(day)
    month = date[1]
    month = remove_leading_zero(month)
    year = date[2]

    hour = time[0]
    minutes = time[1]

    hour = remove_leading_zero(hour)
    minutes = remove_leading_zero(minutes)

    date_result = '{} {} {} year' .format(day, MONTH_NUMBER[month], year)
    if hour == '1':
        hour_string = 'hour'
    else:
        hour_string = 'hours'

    if minutes == '1':
        minutes_string = 'minute'
    else:
        minutes_string = 'minutes'
    time_result = '{} {} {} {}' .format(hour, hour_string, minutes, minutes_string)

    return date_result + ' ' + time_result

if __name__ == '__main__':

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes"
    print("Coding complete? Click 'Check' to earn cool rewards!")
