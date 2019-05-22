def main():
    n = int(input())
    students = []
    for x in range(n):
        name = input()
        score = float(input())

        students.append([name, score])

    print(students)

    smallestScore = students[0][1]

    for student in students:

        if smallestScore > student[1]:
            smallestScore = student[1]
            smallestName = student[0]

    print("student {} has the smallest score of {} " .format(smallestName, smallestScore))

if __name__ == '__main__':
    main()