import time


def calcWastedTime():
    wastingTime = 1

    for i in range(1, 100000):
        wastingTime = wastingTime * i
    return wastingTime

def main():
    startTime = time.time()
    wastedTime = calcWastedTime()
    endTime = time.time()

    print("Start time was {}, end time was {}\n It took {} seconds to finish" . format(startTime,endTime, endTime - startTime))

if __name__ == "__main__":
    main()