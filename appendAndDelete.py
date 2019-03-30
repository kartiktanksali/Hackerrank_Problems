#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:04:58 2019

@author: kartiktanksali
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    
    l = len(set(s).intersection(t))
    print(l)
    if (len(s)-l) + (len(t)-l) <= k:
        return "Yes"
    else:
        return "No"
    

if __name__ == '__main__':
    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    print(result)
