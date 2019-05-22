
def main():

    n = int(input())
    student_marks = {}
    scores = []
    for x in range(n):
        userInput = input()
        userInput = userInput.split()
        hasName = False
        for y in userInput:

            if hasName == False:
                name = y
                hasName = True
            else:
                scores.append(y)
        student_marks[name] = scores
        scores = []


    print(student_marks)
    queryName = input()



    count = 0
    suma = 0
    for k, v in student_marks.items():
        if k == queryName:
            for x in v:
                count += 1
                suma += float(x)
            print("{}" .format(suma/count))


if __name__ == "__main__":
    main()