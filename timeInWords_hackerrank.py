#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:24:58 2019

@author: kartiktanksali
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    ByOne=[0,'one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve',
       'thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','ninteen','twenty']
    ByQua=["%s o' clock", "quarter past %s", "half past %s", "quarter to %s"]
    for i in range(1,10):
        ByOne.append('twenty %s'%ByOne[i])
    
    hour=ByOne[h] if (m<31) else ByOne[h+1]
    if not m%15:
        print(ByQua[m//15] % hour)
    elif m<30:
        return ("%s minute"%ByOne[m]+"s"*(m==1)+ " past %s"%hour)
    else:
        return ("%s minute"%ByOne[60-m]+"s"*(m==59)+ " to %s"%hour)
        
    

if __name__ == '__main__':


    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    print(result)

