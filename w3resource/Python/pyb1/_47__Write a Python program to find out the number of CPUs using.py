#47. Write a Python program to find out the number of CPUs using
import multiprocessing

def get_number_of_cpu():
    return multiprocessing.cpu_count()

def main():
    # These "asserts" are used for self-checking and not for testing
    assert get_number_of_cpu() == 4
    print('Testing completed!')

if __name__ == "__main__":
    main()

