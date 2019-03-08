#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    count=0
    rev=0
    for l in range(i,j+1):
        l = str(l)
        rev = l[::-1]
        rev = int(rev)
        l = int(l)
        if (l-rev)%k==0:
            count+=1
    return count
        
    
if __name__ == '__main__':
    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    print(result)
