import sys
import fileinput

def read_input(f):
    if not f:
        raise Exception("invalid file")
    
    numCycles_list = []
    for line in fileinput.input(f):
        if not fileinput.isfirstline():
            numCycles_list.append(int(line.strip()))
    return numCycles_list

def calculate_height(numCycles):
    defaultHeight = 1
    if (numCycles == 0):
        return defaultHeight
    if (numCycles % 2 == 0):
        return defaultHeight + calculate_height(numCycles-1)
    else:
        return defaultHeight * 2 * calculate_height(numCycles-1)

def main():
    numCycles = read_input("utopian_tree.txt")
    for n in range(len(numCycles)):
        print calculate_height(numCycles[n])
        
if __name__ == '__main__':
    main()