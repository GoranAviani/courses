def is_leap(year):

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:

                return False
        else:
            return True
    else:
        return False


def main():
    year = int(input())
    result = is_leap(year)
    print(result)


if __name__ == "__main__":
    main()