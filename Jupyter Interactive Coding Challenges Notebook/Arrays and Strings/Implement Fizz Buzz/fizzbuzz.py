

class FizzBuzz(object):

    def fizz_buzz(self, number):
        result = []
        if number == 0:
            raise ValueError("Number can't be zero.")
        elif number is None:
            raise TypeError("Number can't be None.")
        else:
            for x in range(1, number+1):
                if (x % 3 == 0) and (x%5 == 0):
                    result.append("FizzBuzz")
                elif x % 3 == 0:
                    result.append("Fizz")
                elif x % 5 == 0:
                    result.append("Buzz")
                else:
                    result.append(str(x))

        return result

