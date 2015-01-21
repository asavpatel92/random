import sys
import math
import fileinput
from _ast import Num
import numbers

def isFibo(number):
    if is_fibonacci(number):
        return "IsFibo"
    else:
        return "IsNotFibo"

def is_fibonacci(n):
    phi = 0.5 + 0.5 * math.sqrt(5.0)
    a = phi * n
    return n == 0 or abs(round(a) - a) < 1.0 / n

def isPerfactSquare(n):
    s = math.sqrt(n)
    return (s * s == n)

def is_fibonacci2(n):
    #n is Fibinacci if one of 5*n*n + 4 or 5*n*n - 4 or both is a perferct square
    if ( isPerfactSquare(5*n*n + 4) or isPerfactSquare(5*n*n - 4)):
        return "IsFibo"
    else:
        return "IsNotFibo"
    
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
    numbers = read_input("isFibo.txt")
    for i in range(len(numbers)):
        print isFibo(numbers[i])
    
if __name__ == '__main__':
    main()