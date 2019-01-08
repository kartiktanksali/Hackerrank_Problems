import math
import os
import random
import re
import sys

# Complete the anotherMinimaxProblem function below.
#def anotherMinimaxProblem(a):

    
    
    
    
    



n = int(input())

a = list(map(int, input().rstrip().split()))

#result = anotherMinimaxProblem(a)
#maximum_or = 0
#temp = 0
#for i in range(len(a)-1):
#    temp = a[i]^a[i+1]
#    print(f"{a[i]} exor {a[i+1]} is {a[i]^a[i+1]}")
#    if temp > maximum_or:
#        maximum_or = temp


#19/23 success algo
#minimum = 0
#maxs = 0
#maximum = []
#temp=0
#for i in range(len(a)-1):
#    for j in range(len(a)):
#        if i!=j:
#            print(f"{a[i]} exor {a[j]} is {a[i]^a[j]}")
#            temp = a[i]^a[j]
#            if temp > maxs:
#                maxs = temp
#            print(f"The Max here is:{maxs}")
#    maximum.append(maxs)
#    maxs=0
#print(min(maximum))   
#
#print(maximum)


#Another Try

#maximum = []
#maxs = 0
#temp = 0
##for i in range(len(a)-1):
##    temp = a[i]^a[i+1]
##    if temp > maxs:
##        maxs = temp
#    
#length = len(a)
#print(length)
#last_element = a[-1]
#print(last_element)
#index = 0
#while a.index(last_element)>0:
#    for j in range(len(a)-1):
#        temp = a[j]^a[j+1]
#        print(f"{a[j]} exor {a[j+1]} is {a[j]^a[j+1]}")
#        if temp > maxs:
#            maxs = temp
#    maximum.append(maxs)
#    maxs=0
#    index = a.index(last_element)
#    a[index],a[index-1] = a[index-1],a[index]
#    
#print(maximum)

#def max_func(i):
#    temp=0
#    maxs=0
    

from itertools import permutations 
perm = permutations(a) 
  
# Print the obtained permutations 
temp = 0
maximum = 0
l = list(perm)
li = []
    
#for i in l:
#    maximum = max_func(i)
#    li.append(maximum)


for k in l:
    for i in range(len(l)):
        for j in range(len(k)-1):
            temp = l[i][j]^l[i][j+1]
            if temp>maximum:
                maximum = temp
        li.append(maximum)
        maximum=0
print(min(li))
        















        