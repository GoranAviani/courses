"""
35. Write a Python program to sort Counter by value. Go to the editor
Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]
"""

from collections import Counter
x = Counter({'Math':81, 'Physics':83, 'Chemistry':87}).most_common()
print(x)