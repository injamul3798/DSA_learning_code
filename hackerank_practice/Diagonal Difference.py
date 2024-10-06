#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

"""
1 2 3
4 5 6
9 8 9  

"""

def diagonalDifference(arr): 
    # Write your code here
    left = 0
    right = 0
    cnt = len(arr)-1
    for i in range(len(arr)):
        left += arr[i][i]
        right += arr[i][len(arr)-i-1]
    return abs(left - right)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
