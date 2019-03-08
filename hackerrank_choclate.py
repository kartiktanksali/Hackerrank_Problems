#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the birthday function below.
def birthday(s, d, m):
    sums = 0
    final_count = 0
    for i in range(len(s)):
        sums += s[i]
        if i > m-1:
            sums -= s[i-m]
        if i >= m-1 and sums==d:
            final_count += 1
    
    return final_count
        


if __name__ == '__main__':

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    print(result)
