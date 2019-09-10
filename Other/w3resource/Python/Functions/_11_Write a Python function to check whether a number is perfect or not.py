def fun(x):
    result = 0
    for n in range(1, x):
       if x % n == 0:
            result += n

    if (((result + x)/2) == x):
      return True
    else:
      return False

if __name__ == '__main__':

  assert fun(6) == True
  assert fun(13) == False
  assert fun(496) == True
  assert fun(495) == False
  assert fun(8128) == True
  assert fun(8130) == False



  print("Testing completed!")