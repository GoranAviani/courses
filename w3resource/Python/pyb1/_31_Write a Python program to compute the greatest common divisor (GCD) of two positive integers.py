#31. Write a Python program to compute the greatest
# common divisor (GCD) of two positive integers.

def get_divisors(number_divisor, number_to_divide):
  all_divisors = []
  for divisor in range(2, number_divisor):
    if number_to_divide % divisor == 0:
      all_divisors.append(divisor)
  return all_divisors


def main():
  common_dividors = []
  greatest_divisor = 0
  user_input = input("Enter 2 numbers separated by comma (,) ")
  user_input = user_input.split(",")
  number_one = user_input[0]
  number_two = user_input[1]
  number_one = int(number_one)
  number_two = int(number_two)
  divisors_for_number_1 = get_divisors(number_one, number_two)
  divisors_for_number_2 = get_divisors(number_two, number_one)

  for x in divisors_for_number_1:
    if x in divisors_for_number_2:
      common_dividors.append(x)

  greatest_divisor = max(common_dividors)
  print(greatest_divisor)
  


if __name__ == "__main__":
  main()
