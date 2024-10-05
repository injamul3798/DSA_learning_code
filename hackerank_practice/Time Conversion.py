#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    len_of_string = len(s)
    last_c = s[len_of_string-1]
    second_l = s[len_of_string-2]
    format_c = second_l + last_c
    if format_c == 'PM':
        
        f_c = s[0]
        f_b = s[1]
        if f_c + f_b == '12':
            fn = f_c + f_b
            
            return s[:len_of_string-2]
        
        fn = f_c + f_b
        final_time = 12 + int(fn)
        
        tmp = str(final_time)
        if len(tmp) == 1:
            # If the converted hour is single digit, we need to prepend '0'
            tmp = '0' + tmp
        return (tmp + s[2:len_of_string-2])
    else:
        f_c = s[0]
        f_b = s[1]
        final_cb = f_c + f_b
        if final_cb == '12':
            return ('00'+s[2:-2])
        else:
            return (s[:-2])
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
