#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 19:36:45 2019

@author: kartiktanksali
"""

n = 4562; 
rev = 0

def reverse(n,rev): 
	while(n > 0): 
	    a = n % 10
	    rev = rev * 10 + a 
	    n = n / 10
	    return rev
      
print(reverse(n,rev)) 