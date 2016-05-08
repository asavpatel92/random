from __future__ import print_function

# import sys
import fileinput

def count_changes(input):
    for item in input[1:]:
        if len(item) % 2 == 0:
            temp = {}
            change = 0
            first = item[:len(item) / 2]
            second = item[len(item) / 2:]
            for char in first:
                temp[char] = temp.get(char, 0) + 1
            for char in second:
                if temp.get(char):
                    temp[char] = temp.get(char) - 1
            for key, value in temp.iteritems():
                change += value
            print (change)
        else:
            print (-1)

def read_input(f):
    if not f:
        raise Exception("invalid file")
    strings = []
    for line in fileinput.input(f):
        strings.append((line.strip()))
    return strings

def main():
#     strings = read_input(sys.stdin)
    strings = read_input("anagram_changes.txt")
    count_changes(strings)

main()
