#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    V = 0
    N = 0
    for step in s:
        if step == "U":
            N += 1
            if N == 0:
                V += 1
        else:
            N -= 1
    return V


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + "\n")

    fptr.close()
