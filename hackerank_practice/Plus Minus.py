#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos_cnt = 0
    neg_cnt = 0
    zero_cnt = 0
    for i in arr:
        if i>0:
            pos_cnt += 1
        elif i<0:
            neg_cnt += 1
        else:
            zero_cnt += 1
            
    total_len = len(arr)
    #formatted_number = f"{number:.6f}"
    pos_ratio = pos_cnt /total_len
    neg_ratio = neg_cnt/total_len
    zero_ratio = zero_cnt / total_len
    
    print(f"{pos_ratio:.6f}")
    print(f"{neg_ratio:.6f}")
    print(f"{zero_ratio:.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
