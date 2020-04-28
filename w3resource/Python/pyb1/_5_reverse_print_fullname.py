#5. Write a Python program which accepts the user's first and last name and print them in reverse
# order with a space between them.

def rev_names(**kwargs):
    try:
        first_name = kwargs["first_name"]
        last_name = kwargs["last_name"]
    except KeyError as e:
        return "Error: {}" .format(e)
    else:
        return ("{} {}".format(first_name[::-1], last_name[::-1]))

parameters = {"first_name": "Goran", "last_name": "Aviani"}
result = rev_names(**parameters)
print(result)