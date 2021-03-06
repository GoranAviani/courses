# 20. Write a Python program to get a string which is n (non-negative integer)
# copies of a given string.

def calc(**kwargs):
    try:
        all_user_inputs = kwargs["all_user_inputs"]
    except KeyError as e:
        return "{}" .format(e)

    times_multiplied = int(all_user_inputs[1])
    base_word = all_user_inputs[0]
    result = ""
    for n in range(0, times_multiplied):
        result += base_word
    return result

def main():
    all_user_inputs = []
    for x in range(0, 2):
        user_input = input("enter value: \n")
        all_user_inputs.append(user_input)

    parameters = {"all_user_inputs": all_user_inputs}
    result = calc(**parameters)
    print(result)


if __name__ == "__main__":
    main()