#47. Write a Python program to find out the number of CPUs using
import multiprocessing
def fun():


    return multiprocessing.cpu_count()
if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    fun() == 4
    print('Testing completed!')

