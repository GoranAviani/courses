#You prefer a good old 12-hour time format.
# But the modern world we live in would rather use the 24-hour format and you see it everywhere. Your task is to convert the time from the 24-h format into 12-h format by following the next rules:
# the output format should be 'hh:mm a.m.' (for hours before midday) or
# 'hh:mm p.m.' (for hours after midday)
#- if hours is less than 10 - don't write a '0' before it.
# For example: '9:05 a.m.'


#24h
#Hh:mm
def time_converter(time):
    #replace this for solution
    #24 h
    #Hh: mm

    result = ""

    time24 = time.split(":")

    time24Num = []
    time24Num.append(int(time24[0]))
    time24Num.append(time24[1])
    #for x in time24:
    #    time24Num.append(int(x))

    if time24Num[0] == 0:
        #print("{}:{} p.m.".format(time24Num[0], time24Num[1]))
        return ("{}:{} a.m.".format(12, time24Num[1]))

    elif time24Num[0] < 12:
        print("{}:{} a.m.".format(time24Num[0], time24Num[1]))
        return ("{}:{} a.m.".format(time24Num[0], time24Num[1]))

    elif time24Num[0] == 12:
        #print("{}:{} p.m.".format(time24Num[0], time24Num[1]))
        return ("{}:{} p.m.".format(time24Num[0], time24Num[1]))

    elif time24Num[0] == 0:
        #print("{}:{} p.m.".format(time24Num[0], time24Num[1]))
        return ("{}:{} p.m.".format(12, time24Num[1]))


    else:
        return ("{}:{} p.m.".format((time24Num[0] - 12), time24Num[1]))

if __name__ == '__main__':
    print("Example:")
    #print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")