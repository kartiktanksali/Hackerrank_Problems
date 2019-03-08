#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    firstday = 5
    cum = 0
    for i in range(n):
        cum += math.floor(firstday/2)
        firstday = math.floor(firstday/2) * 3
    return cum

if __name__ == '__main__':
    n = int(input())

    result = viralAdvertising(n)

    print(result)
