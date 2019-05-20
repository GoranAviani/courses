def main():
    noOfStudents = input()
    result = []

    for x in range(0, int(noOfStudents)):
        stuName = input()
        stuGrade = input()
        result.append([stuName, stuGrade])

    for x in result:
        lowName = ""
        lowGrade = ""
        lowGrade = x[1]
        lowName = x[0]

        if x[1] < lowGrade:
            lowGrade = x[1]
            lowName = x[0]

    print(lowName)



if __name__ == "__main__":
    main()