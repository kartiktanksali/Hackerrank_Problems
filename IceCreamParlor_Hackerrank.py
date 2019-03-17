#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the icecreamParlor function below.
def icecreamParlor(m, arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i!=j:
                if arr[i]+arr[j]==m:
                    i+=1
                    j+=1
                    if i<j:
                        return f"{i} {j}"
                    else:
                        return f"{j} {i}"
    
    
if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        print(result)