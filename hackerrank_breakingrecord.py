#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    minimum = scores[0]
    maximum = scores[0]
    count_min = 0
    count_max = 0
    lst = []
    for i in scores:
        if i<minimum:
            minimum=i
            count_min += 1
        if i>maximum:
            maximum=i
            count_max += 1
    lst.append(count_max)
    lst.append(count_min)
    return lst

if __name__ == '__main__':

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(result)
