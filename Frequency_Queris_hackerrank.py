#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 13:28:24 2019

@author: kartiktanksali
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    fre_tab = {}
    lst = []
    for i in queries:
        if i[0]==1:
            if i[1] in fre_tab:
                fre_tab[i[1]] += 1
            else:
                fre_tab[i[1]] = 1
        elif i[0]==2:
            if i[1] in fre_tab:
                if fre_tab[i[1]]==0:
                    del fre_tab[i[1]]
                elif fre_tab[i[1]]>0:
                    fre_tab[i[1]]-=1
        elif i[0]==3:
            if i[1] in fre_tab.values:
                lst.append(1)
            else:
                lst.append(0)
    
    return lst

if __name__ == '__main__':

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    print('\n'.join(map(str, ans)))
    print('\n')

