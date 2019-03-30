#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 11:11:19 2019

@author: kartiktanksali
"""

def atMostSum(arr,k): 
    _sum = 0
    cnt = 0
    maxcnt = 0
      
    for i in range(len(arr)): 
  
        if ((_sum + arr[i]) <= k): 
            _sum += arr[i] 
            cnt += 1
          
        elif(sum != 0): 
            _sum = _sum - arr[i - cnt] + arr[i] 
          
        maxcnt = max(cnt, maxcnt) 
  
    return maxcnt 

arr = [1,2,3,4,5]
k = 6

res = atMostSum(arr,k)
print(res)
