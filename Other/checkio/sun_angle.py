"""
 Every true traveler must know how to do 3 things:
 fix the fire, find the water and extract useful information from the nature around him.
 Programming won't help you with the fire and water, but when it comes to the
 information extraction - it might be just the thing you need.

Your task is to find the angle of the sun above the horizon knowing the time of the day.
Input data: the sun rises in the East at 6:00 AM, which corresponds to the angle of 0 degrees.
At 12:00 PM the sun reaches its zenith, which means that the angle equals 90 degrees.
6:00 PM is the time of the sunset so the angle is 180 degrees.
If the input will be the time of the night (before 6:00 AM or after 6:00 PM),
your function should return - "I don't see the sun!".

 Input: The time of the day.

Output: The angle of the sun, rounded to 2 decimal places.

Example:
sun_angle("07:00") == 15
sun_angle("12:15"] == 93.75
sun_angle("01:23") == "I don't see the sun!"
"""
from datetime import datetime

def sun_angle(time: str):
    time = datetime.strptime(time,'%H:%M')
    sunrise = '06:00'
    sunrise = datetime.strptime(sunrise,'%H:%M')
    sunset = '18:00'
    sunset = datetime.strptime(sunset, '%H:%M')
    midnight_00 = datetime.strptime('00:00', '%H:%M')
    midnight_24 = datetime.strptime('23:59', '%H:%M')
    if (time > sunset and time < midnight_24) or (time < sunrise and time > midnight_00):
        return "I don't see the sun!"


    return time

if __name__ == '__main__':

    #These "asserts" using only for self-checking and not necessary for auto-testing
    #assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
