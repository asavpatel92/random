from __future__ import print_function
# import sys
import fileinput

def game_of_thrones(string):
    found = False
    # Write the code to find the required palindrome and then assign the variable 'found' a value of True or False
    dict = {}
    
    for i in range(len(string)):
        ch = string[i]
        if ch in dict:
            dict[ch] += 1
        else:
            dict[ch] = 1
    
    chars_whose_count_is_odd = 0
    for key, value in dict.items():
        if value % 2 == 1:
            chars_whose_count_is_odd += 1
    
    if chars_whose_count_is_odd > 1:
        found = False
    else:
        found = True
    
    if not found:
        return "NO"
    else:
        return "YES"

def read_input(f):
    if not f:
        raise Exception("invalid file")
    string = None
    for line in fileinput.input(f):
        string = line.strip()
    return string

def main():
    # string = read_input(sys.stdin)
    string = read_input("game_of_thrones.txt")
    print (game_of_thrones(string))

main()