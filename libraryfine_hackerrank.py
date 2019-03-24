#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 18:11:58 2019

@author: kartiktanksali
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the libraryFine function below.
def libraryFine(d1, m1, y1, d2, m2, y2):
    
    if d1>d2 and m1==m2 and y1==y2:
        return abs((d1-d2)*15)
    elif m1>m2 and y1==y2:
        return abs(m1-m2)*500
    elif y1>y2:
        return 10000
    else:
        return 0

if __name__ == '__main__':

    d1M1Y1 = input().split()

    d1 = int(d1M1Y1[0])

    m1 = int(d1M1Y1[1])

    y1 = int(d1M1Y1[2])

    d2M2Y2 = input().split()

    d2 = int(d2M2Y2[0])

    m2 = int(d2M2Y2[1])

    y2 = int(d2M2Y2[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    print(result)
