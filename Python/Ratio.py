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
    # Write your code here
    pos = 0
    neg = 0
    zero = 0
    for i in arr:
        if i < 0:
            neg += 1
        elif i > 0:
            pos += 1
        else:
            zero += 1
    n = len(arr)
    
    rpos = pos/n
    rneg = neg/n
    rero = zero/n
    
    print(f"{rpos:.6f}")
    print(f"{rneg:.6f}")
    print(f"{rero:.6f}")
