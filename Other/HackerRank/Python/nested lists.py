def main():
    n = int(input())
    students = []
    for x in range(n):
        name = input()
        score = float(input())

        students.append([name, score])

    print(students)




if __name__ == '__main__':
    main()