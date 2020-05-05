#_37_Write a Python program to display your details like
# name, age, address in three different lines
def fun(name, age, address):
    result = name + "\n" + age + "\n" + address
    return result

def main():
    # These "asserts" are used for self-checking and not for testing
    assert fun('Goran', '32', 'Stockholm') == 'Goran\n32\nStockholm'
    print('Testing completed!')
    
if __name__ == '__main__':
    main()
