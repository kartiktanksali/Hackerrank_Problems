#!/bin/python3

import math
import os
import random
import re
import sys

    

if __name__ == '__main__':
    s = input()

#    result = encryption(s)
    c = math.ceil(math.sqrt(len(s)))
    print(" ".join(map(lambda x: s[x::c],range(c))))
        
        
