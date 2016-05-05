# https://www.hackerrank.com/challenges/angry-children

import fileinput

def max_min(N, K, lists):
    lists.sort()
    min_val = lists[-1]

    for i in range(0, len(lists) - K + 1):
    
        temp_min = lists[i]
        temp_max = lists[i + K - 1]
        temp_diff = temp_max - temp_min
        if temp_diff < min_val:
            min_val = temp_diff
                
    return min_val

def read_input(f):
    if not f:
        raise Exception("invalid file")
    temp = []
    for line in fileinput.input(f):
        temp.append((int(line.strip())))
    return temp

def main():
    # input = read_input(sys.stdin)
    input = read_input("max_min.txt")
    assert max_min(input[0], input[1], input[2:]) == 3
    
main()
