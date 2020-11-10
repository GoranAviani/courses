def add_five(x):
  return x + 5

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)

nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))
print(res)


def countdown():
  i = 5
  while i > 0:
    yield i
    i -= 1


for i in countdown():
  print(i)


  def infinite_sevens():
    while True:
      yield 7


  for i in infinite_sevens():
    print(i)