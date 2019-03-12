import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    '''for i in range(len(p)):
        i = i+1
        ind = p.index(i)
        ind = ind+1
        ind_n = p.index(ind)
        print(ind_n+1)
    '''
    #Another option
    return [p.index(p.index(i+1)+1)+1 for i in range(len(p))]

if __name__ == '__main__':
    

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    print("\n".join(map(str,result)))