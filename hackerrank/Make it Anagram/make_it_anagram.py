from __future__ import print_function
# import sys
import fileinput

def make_it_anagram(str1, str2):
    temp = {}
    count = 0
    if sorted(str1) != sorted(str2):
        for char in str1:
            temp[char] = temp.get(char, 0) + 1
        
        for char in str2:
            if temp.get(char):
                temp[char] -= 1
            else:
                count += 1
        
        for entry in temp:
            if temp.get(entry) > 0:
                count = count + temp.get(entry)
    return count
    
def read_input(f):
    if not f:
        raise Exception("invalid file")
    strings = []
    for line in fileinput.input(f):
        strings.append((line.strip()))
    return strings

def main():
    #strings = read_input(sys.stdin)
    strings = read_input("make_it_anagram.txt")
    print (make_it_anagram(strings[0], strings[1]))

main()