#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the taumBday function below.
def taumBday(b, w, bc, wc, z):
    totalcost = 0
    if z < (bc|wc):
        if bc>wc:
            if (wc+z)<bc:
                totalcost=(wc*w)+((wc+z)*b)
            else:
                totalcost=(bc*b)+(wc*w)
        else:
            if (bc+z)<wc:
                totalcost=(bc*b)+((bc+z)*w)
            else:
                totalcost=(bc*b)+(wc*w)
    else:
        totalcost=(bc*b)+(wc*w)
    return totalcost

if __name__ == '__main__':
    

    t = int(input())

    for t_itr in range(t):
        bw = input().split()

        b = int(bw[0])

        w = int(bw[1])

        bcWcz = input().split()

        bc = int(bcWcz[0])

        wc = int(bcWcz[1])

        z = int(bcWcz[2])

        result = taumBday(b, w, bc, wc, z)

        print(result)
    
