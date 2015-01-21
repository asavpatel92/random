# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import fileinput
from _ast import Num
import numbers

def find_digits(numbers):
    number_string = str(numbers)
    digits = 0
    for digit in number_string:
        if(int(digit) == 1):
            digits += 1
        elif(int(digit) > 0 and int(numbers)%int(digit) == 0):
            digits += 1
    return digits
                
    
def read_input(f):
    if not f:
        raise Exception("invalid file")
    numbers = []
    for line in fileinput.input(f):
        if not fileinput.isfirstline():
            numbers.append(int(line.strip()))
    return numbers

def main():
    #numbers = read_input(sys.stdin)
    numbers = read_input("find_digits.txt")
    for i in range(len(numbers)):
        print find_digits(numbers[i])
    
if __name__ == '__main__':
    main()