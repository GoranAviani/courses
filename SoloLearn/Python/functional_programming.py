def apply_twice(func, arg):
   return func(func(arg))

def add_five(x):
   return x + 5

print(apply_twice(add_five, 10))

def pure_function(x, y):
  temp = x + 2*y
  return temp / (2*x + y)

some_list = []

def impure(arg):
  some_list.append(arg)

  y = x ** 2
  z = x + y
  return z

def my_func(f, arg):
  return f(arg)

my_func(lambda x: 2*x*x, 5)