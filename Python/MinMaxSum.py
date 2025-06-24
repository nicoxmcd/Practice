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
    min = 10 ** 9
    max = 0
    sum = 0
    for i in arr:
        if i > max:
            max = i
        if i < min:
            min = i
        sum += i
     
    minsum = sum - max
    maxsum = sum - min   
    
    print(str(minsum) + " " + str(maxsum))
            
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
