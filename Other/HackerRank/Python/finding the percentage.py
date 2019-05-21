
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



if __name__ == "__main__":
    main()