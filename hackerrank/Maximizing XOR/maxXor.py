#!/bin/python
import math

# Complete the function below.


def  maxXor( l,  r):
    return max(A ^ B for A in range(l, r + 1) for B in range(l, r + 1))

def main():
    _l = int(raw_input());
    _r = int(raw_input());
    res = maxXor(_l, _r);
    print(res)

if __name__ == '__main__':
    main()
