import sys
"""
Note :: please read this nice article about how to generate next lexicographical permutation
https://www.nayuki.io/page/next-lexicographical-permutation-algorithm

it's much easier to think about this problem in terms of numbers than character
Example: 5 1 4 3 2 0 =>  5 2 4 3 1 0 => 5 2 0 1 3 4 
We want to increase this sequence by as little as possible using same digits. 

Step1 :: find the increasing sequence from the end, 4320 in this case, lets call it a suffix
Step2 :: Mark digit 1 (just before 4) as pivot 
Step3 :: Swap the smallest number in suffix which is greater than pivot, i.e. swap 1 with 2 => 5 2 4 3 1 0
Step4 :: as suffix increased, i.e we went from 51 to 52, so we want to make suffix as small as possible
         sort the suffix , which will make it smallest possible suffix => 5 2 0 1 3 4 
         
"""

def next_bigger(s):
    # easier to work with list and indexes
    lst = list(s)

    # Step 1
    # find longest increasing sequence from end
    index = len(lst) - 1
    while index > 0:
        if lst[index-1] < lst[index]:
            break
        index -= 1

    # the whole string is decreasing 
    if index == 0:
        return 'no answer'

    # Step 2
    # suffix is end to index
    suffix_start = index
    pivot = index - 1
    #print "suffix:", lst[suffix_start:]

    # Step 3
    for index in range(len(s)-1, suffix_start-1, -1):

        # this will be the next bigger element than the pivot
        if lst[index] > lst[pivot]:
            break

    lst[index], lst[pivot] = lst[pivot], lst[index]

    # Step 4
    # now sort the suffix, reversing it will sort it as it's a decreasing sequence
    sorted_suffix = sorted(lst[suffix_start:])
    return ''.join(lst[:suffix_start] + sorted_suffix)


def read_input(f):
    linenum = 0
    for line in f.readlines():
        linenum += 1
        if linenum == 1:
            continue
        yield line.strip()

def main():
    for line in read_input(sys.stdin):
        print "%s" % next_bigger(line)

if __name__ == "__main__":
    main()

