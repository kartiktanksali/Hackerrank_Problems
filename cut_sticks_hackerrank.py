#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 22:32:45 2019

@author: kartiktanksali
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    top=len(arr)-1
    arr.sort(reverse=True)
    while(len(arr)>1):
        print(len(arr))
        m = min(arr)
        while(arr[top]==m):
            arr.pop()
            top=top-1
        
    print(len(arr))

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    cutTheSticks(arr)

    

