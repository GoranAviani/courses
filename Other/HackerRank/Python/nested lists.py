def main():
    n = int(input())
    students = []

    #getting all students and their scores
    for x in range(n):
        name = input()
        score = float(input())

        students.append([name, score])

    #print(students)

    biggestScore = students[0][1]
    biggestName = students[0][0]
    #finding the student with the smallest score
    for student in students:
        if biggestScore < student[1]:
            biggestScore = student[1]
            biggestName = student[0]


    #print("student {} has the biggest score of {} " .format(biggestName, biggestScore))


    smallestScore = biggestScore
    smallestScore2 = smallestScore
    #finding student/s with the second smallest score
    for y in students:
        if smallestScore > y[1]:
            smallestScore2 = smallestScore
            smallestScore = y[1]
        elif y[1] > smallestScore and y[1] < smallestScore2:
            smallestScore2 = y[1]

# 4 3 1 -1 0
    #print("smallest score is {}, second smallest score is {}" .format(smallestScore, smallestScore2))


    #finding all students with second smallest score
    result = []
    for x in students:
        if x[1] == smallestScore2:
            result.append(x[0])


    #printing results
    result = sorted(result)
    for x in result:
        print(x)

if __name__ == '__main__':

    main()