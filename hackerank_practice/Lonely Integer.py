#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    hash_map = {}
    for i in a:
        if i not in hash_map:
            hash_map[i] = 1
        else:
            hash_map[i] += 1
    for key,items in hash_map.items():
        if items ==1 :
            return key

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
