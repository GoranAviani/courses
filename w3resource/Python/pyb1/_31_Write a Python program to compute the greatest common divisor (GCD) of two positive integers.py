#31. Write a Python program to compute the greatest
# common divisor (GCD) of two positive integers.
def get_greatest_number_in_list(list_of_numbers):
  return max(list_of_numbers)

def get_common_numbers_from_two_lists(list1, list2):
  common_dividors = []
  for x in list1:
    if x in list2:
      common_dividors.append(x)
  return common_dividors


def get_divisors(number_divisor, number_to_divide):
  all_divisors = []
  for divisor in range(2, number_divisor):
    if number_to_divide % divisor == 0:
      all_divisors.append(divisor)
  return all_divisors

def get_user_input(number_of_inputs):
  user_input = []
  for number_of_input in range(1, number_of_inputs +1):
    keystrokes = input("Enter number {}: ".format(number_of_input))
    user_input.append(keystrokes)

  return user_input

def main():
  user_input = get_user_input(2)
  number_one = user_input[0]
  number_two = user_input[1]
  number_one = int(number_one)
  number_two = int(number_two)
  divisors_for_number_1 = get_divisors(number_one, number_two)
  divisors_for_number_2 = get_divisors(number_two, number_one)

  common_dividors = get_common_numbers_from_two_lists(divisors_for_number_1, divisors_for_number_2)
  greatest_divisor = get_greatest_number_in_list(common_dividors)
  print(greatest_divisor)

if __name__ == "__main__":
  main()
