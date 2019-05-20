
def main():
    result = []
    x, y, z, n = int(input()), int(input()), int(input()), int(input())
    if x + y + z != n:
        for x in range (0,x+1):
            for y in range (0, y+1):
                for z in range(0, z + 1):
                    if x + y + z != n:
                      #  print("{} {} {}" .format(x,y,z))
                        result.append([x,y,z])


    print(result)
if __name__ == "__main__":
    main()