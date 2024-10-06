#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
   hash_map = {}
   results = [0] * 100
   
   for i in range(len(arr)):
       if arr[i] not in hash_map:
           hash_map[arr[i]] = 1
           results[arr[i]] = hash_map[arr[i]]
       else:
           hash_map[arr[i]] += 1
           results[arr[i]] = hash_map[arr[i]]
           
   return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
