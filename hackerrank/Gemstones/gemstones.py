from __future__ import print_function
# import sys
import fileinput

def gemstones(stones):
    gems = {}
    count = 0
    no_of_stones = int(stones[0])
    for stone in stones[1:]:
        for char in "".join(set(stone)):
            gems[char] = gems.get(char, 0) + 1
    for gem in gems:
        if gems.get(gem) == no_of_stones:
            count += 1
    return count
    

def read_input(f):
    if not f:
        raise Exception("invalid file")
    stones = []
    for line in fileinput.input(f):
        stones.append((line.strip()))
    return stones

def main():
    # stones = read_input(sys.stdin)
    stones = read_input("gemstones.txt")
    print (gemstones(stones))

main()
