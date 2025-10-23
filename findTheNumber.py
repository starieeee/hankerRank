#!/bin/python

import math
import os
import random
import re
import sys


#
# Complete the 'findNumber' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER k
#

def findNumber(arr, k):
    # Write your code here
    if k in arr:
        return "YES"
    else:
        return "NO"
            
def main():
    print(findNumber([1,2,3,4,5], 3))
main()