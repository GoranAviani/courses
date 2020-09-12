"""


Michael always knew that there was something wrong with his family. Many strangers were introduced to him as part of it.

Michael should figure this out. He's spent almost a month parsing the family archives. He has all father-son connections of his entire family collected in one place.

With all that data Michael can easily understand who the strangers are. Or maybe the only stranger in this family is Michael? Let's see.

You have a list of family ties between father and son. Each element on this list has two elements. The first is the father's name, the second is the son's name. All names in the family are unique. Check if the family tree is correct. There are no strangers in the family tree. All connections in the family are natural.

Input: list of lists. Each element has two strings. The list has at least one element

Output: bool. Is the family tree correct.

Example:
is_family([
  ['Logan', 'Mike']
]) == True
is_family([
  ['Logan', 'Mike'],
  ['Logan', 'Jack']
]) == True
is_family([
  ['Logan', 'Mike'],
  ['Logan', 'Jack'],
  ['Mike', 'Alexander']
]) == True
is_family([
  ['Logan', 'Mike'],
  ['Logan', 'Jack'],
  ['Mike', 'Logan']
]) == False  # Can you be a father for your father?
is_family([
  ['Logan', 'Mike'],
  ['Logan', 'Jack'],
  ['Mike', 'Jack']
]) == False  # Can you be a father for your brother?
is_family([
  ['Logan', 'William'],
  ['Logan', 'Jack'],
  ['Mike', 'Alexander']
]) == False  # Looks like Mike is a stranger in Logan's family
"""


def is_family(tree):
    return True


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_family([
      ['Logan', 'Mike']
    ]) == True, 'One father, one son'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack']
    ]) == True, 'Two sons'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Alexander']
    ]) == True, 'Grandfather'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Logan']
    ]) == False, 'Can you be a father to your father?'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Jack']
    ]) == False, 'Can you be a father to your brother?'
    assert is_family([
      ['Logan', 'William'],
      ['Logan', 'Jack'],
      ['Mike', 'Alexander']
    ]) == False, 'Looks like Mike is stranger in Logan\'s family'
    print("Looks like you know everything. It is time for 'Check'!")
