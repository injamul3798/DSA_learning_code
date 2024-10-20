#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    mx = 0
    mn = 0
    for i in range(0,4):
        mn += arr[i]
    for i in range(len(arr)-1,len(arr)-5,-1):
        mx += arr[i]
    print(f'{mn} {mx}')
    #print(mx)
        
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
