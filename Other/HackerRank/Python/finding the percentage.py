
def main():

    n = int(input())
    student_marks = {}
    scores = []
    for x in range(n):
        userInput = input()
        userInput = userInput.split()
        for y in userInput:
            hasName = False
            if hasName == False:
                name = y
                hasName = True
            else:
                scores.append(y)
        scores = []
        student_marks[name] = scores

    print(student_marks)
    queryName = input()



if __name__ == "__main__":
    main()