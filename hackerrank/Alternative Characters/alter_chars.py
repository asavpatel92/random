import sys
import fileinput

def read_input(f):
    if not f:
        raise Exception("invalid file")
    strings_list = []
    for line in fileinput.input(f):
        if not fileinput.isfirstline():
            strings_list.append(str(line.strip()))
    return strings_list

def makeAlternate(stringInput):
    chars = list(stringInput)
    counter = 0
    for i in range(len(chars)-1):
        if( chars[i] == chars[i+1]):
            counter += 1
    return counter

def main():
    #strings_list = read_input(sys.stdin)
    strings_list = read_input("alter_chars.txt")
    for stringInput in range(len(strings_list)):
        print makeAlternate(strings_list[stringInput])
    
if __name__ == '__main__':
    main()