#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 14:51:38 2019

@author: kartiktanksali
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the minimumDistances function below.
def minimumDistances(a):
   lst = []
   
   for i in range(len(a)):
       for j in range(len(a)):
           if i!=j:
               if a[i]==a[j]:
                   lst.append(abs(i-j))
   lst.sort()
   if lst!=[]:         
       return lst[0]
   else:
       return -1
    
    
    
    

if __name__ == '__main__':
    
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    print(result)
