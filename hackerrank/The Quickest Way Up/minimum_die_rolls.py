import sys
"""
solution to the problem of Snakes and Ladders (https://www.hackerrank.com/challenges/the-quickest-way-up)
we can do a BFS to find shortest path to get to 100
"""

def get_neighbors(square, ladders, snakes):
    """
    where can you go from given square 
    """

    for next_square in range(square, square+6+1):
        if next_square in ladders:
            yield ladders[next_square]
        elif next_square in snakes:
            yield snakes[next_square]
        else:
            yield next_square

def get_path(frm, parents):

    if frm not in parents:
        return ''

    return str(parents.get(frm, '')) + "," + get_path(parents.get(frm, ''), parents)

def BFS(ladders, snakes, source=0, destination=100):
    current_square = 0
    total_rolls = 0
    done = False
    parents = {}
    queue = [(source, 0)]
    parents[source] = ''

    while queue:
        current_square, num_rolls = queue.pop(0)
        for next_square in get_neighbors(current_square, ladders, snakes):
            if next_square in parents:
                continue
     
            parents[next_square] = current_square
            queue.append((next_square, num_rolls+1))

            if next_square == destination:
                return num_rolls+1, get_path(next_square, parents)
    
    return -1, None

def test_input(f=None):
    test_cases = []
    ladders = {32: 62, 42: 68, 12: 98}
    snakes = {95:13, 97:25, 93: 37, 79: 27, 75: 19, 49: 47, 67:17}
    test_cases.append((ladders, snakes))
    ladders = {8: 52, 6: 80, 26: 42, 2: 72, 4: 94}
    ladders = {8: 52, 6: 80, 26: 42, 2: 72}
    snakes = {51: 19, 39: 11, 37: 29, 81: 3, 59: 5, 79: 23, 53: 7, 43: 33, 77: 21, 95:0, 96: 0, 97:0, 98: 0, 99:0, 100:0}
    snakes = {51: 19, 39: 11, 37: 29, 81: 3, 59: 5, 79: 23, 53: 7, 43: 33, 77: 21}
    test_cases.append((ladders, snakes))
    return test_cases

def read_input():
    test_cases = []
    linenum = 0
    total_cases = int(input())
    for case in range(total_cases):
        ladders = {}
        snakes = {}
        total_ladders = int(input())
        for _ in range(total_ladders):
            ladder = raw_input().strip()
            start, stop = ladder.split()
            ladders[int(start)] = int(stop)

        total_snakes = int(raw_input())
        for _ in range(total_snakes):
            snake = raw_input().strip()
            start, stop = snake.split()
            snakes[int(start)] = int(stop)

        test_cases.append((ladders, snakes))
    return test_cases

def main():
    #for ladders, snakes in test_input():
    for ladders, snakes in read_input():
        rolls, path = BFS(ladders, snakes, 1)
        print rolls
        #print "================"

if __name__ == "__main__":
    main()
