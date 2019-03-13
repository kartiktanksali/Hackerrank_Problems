#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    fact=1
    if n<0:
        print("Sorry cannot determine the factorial")
    elif n==0:
        print(0)
    else:
        for i in range(1,n+1):
            fact = fact*i
    print(fact)
    

if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
