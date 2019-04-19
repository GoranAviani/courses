#4. Write a Python script to check if a given key already exists in a dictionary.


exdict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


def does_it_have_a_key(key):
    has_key = False
    for x in exdict:
        if x == key:
            has_key = True

    if has_key == True:
        print("it has that key")
    else:
         print("the key is not there")

does_it_have_a_key(5)
does_it_have_a_key(9)