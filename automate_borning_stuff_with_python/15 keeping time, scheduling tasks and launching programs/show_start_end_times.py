import time


def calcWastedTime():
    wastingTime = 1

    for i in range(1, 100000):
        wastingTime = wastingTime * i
    return wastingTime

def main():
    startTime = round(time.time(), 2)
    wastedTime = calcWastedTime()
    endTime = round(time.time(), 2)

    print("Start time was {}, end time was {}\n It took {} seconds to finish" . format(startTime,endTime, round(endTime - startTime, 2)))

if __name__ == "__main__":
    main()