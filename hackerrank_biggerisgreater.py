#!/bin/python3

import math
import os
import random
import re
import sys

#Complete the biggerIsGreater function below.
def checkifeq(lst):
    return all(x==lst[0] for x in lst)


def biggerIsGreater(w):
    lst_ord = [ord(i) for i in w]
    temp_lst = ""
    final_lst = []
    if checkifeq(lst_ord)==True:
        return "no answer"
    else:
        for i in range(len(lst_ord)):
            if lst_ord[i]<lst_ord[i+1]:
                temp = lst_ord[i]
                lst_ord[i] = lst_ord[i+1]
                lst_ord[i+1] = temp
                temp_lst = "".join([chr(j) for j in lst_ord])
                final_lst.append(temp_lst)
        return final_lst


if __name__ == '__main__':

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        print(result)

    
