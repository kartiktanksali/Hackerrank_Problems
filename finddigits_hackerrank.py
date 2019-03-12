#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    number = map(int,str(n))
    count=0
    for i in number:
        if i>0:
            if n%i==0:
                count+=1
    return count
        

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        print(result)
    