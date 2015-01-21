import sys
import fileinput
from itertools import islice
def read_input(f):
    if not f:
        raise Exception("invalid file")
    strings_list = []
    for line in fileinput.input(f):
        if not fileinput.isfirstline():
            strings_list.append(str(line.strip()))
    return strings_list
   
def getNumRotations(word):
    difference = lambda x, y: abs(ord(x) - ord(y))
    median = len(word) // 2
    pairs = zip(word, reversed(word))
    operations = sum(difference(x, y) for x, y in islice(pairs, median))
    return operations

def main():
    #strings_list = read_input(sys.stdin)
    strings_list = read_input("TheLoveLetterMystery.txt")
    for word in range(len(strings_list)):
        print getNumRotations(strings_list[word])
    
    
if __name__ == '__main__':
    main()