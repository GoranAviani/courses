list = [1, 1, 2, 3, 5, 8, 13]
print(list[4])
print(list[list[4]])




def shortest_string(x, y):
  if len(x) <= len(y):
    return x
  else:
  	return y



def shout(word):
	return word + "!"
	speak = shout
	output = speak("shout")
	print(output)

#Many third-party Python modules are stored on the Python Package Index (PyPI).
#The best way to install these is using a program called pip. This comes installed by default with modern distributions of Python.


def sum(x):
  res = 0
  for i in range(x):
    res += i
  return res


def print_nums(x):
for i in range(x):
	print(i)
	return
print_nums(10)


def func(x):
res = 0
	for i in range(x):
	res += i
	return res

print(func(4))


#Different exceptions are raised for different reasons.
#Common exceptions:
#ImportError: an import fails;
#IndexError: a list is indexed with an out-of-range number;
#NameError: an unknown variable is used;
#SyntaxError: the code can't be parsed properly;
#TypeError: a function is called on a value of an inappropriate type;
#ValueError: a function is called on a value of the correct type, but with an inappropriate value.











