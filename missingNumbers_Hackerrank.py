#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 17:06:52 2019

@author: kartiktanksali
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    lst = []
    arr_hash = Counter(arr)
    brr_hash = Counter(brr)
     
    for i in brr_hash.keys():
        if i not in arr_hash:
            lst.append(i)
        elif brr_hash[i]!=arr_hash[i]:
            lst.append(i)
    
    lst.sort()
    return lst
    

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    print(' '.join(map(str, result)))
    