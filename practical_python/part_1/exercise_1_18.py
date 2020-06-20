"""
Exercise 1.18: Regular Expressions
"""
import re

def main():
    text = 'Today is 3/27/2018. Tomorrow is 3/28/2018.'
    all_occurances = re.findall(r'\d+/\d+/\d+', text)
    print(all_occurances)
    all_occurances = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
    print(all_occurances)

if __name__ == '__main__':
    main()