'''
9. Write a Python program to display the examination schedule. (extract the date from exam_st_date). Go to the editor
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
'''

def main():
    exam_st_date = (11, 12, 2014)
    print("The examination will start from : {} / {} / {}" . format(exam_st_date[0], exam_st_date[1], exam_st_date[2]))

if __name__ == "__main__":
    main()