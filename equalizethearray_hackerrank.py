#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the equalizeArray function below.
def equalizeArray(arr):
    mode = Counter(arr)
    m = mode.most_common(1)[0][0]
    delCount = 0
    for i in arr:
        if i!=m:
            delCount+=1
    return delCount

if __name__ == '__main__':
    

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    print(result)
