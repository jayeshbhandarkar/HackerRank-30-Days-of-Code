import math
import os
import random
import re
import sys

def bitwiseAnd(N, K):
    max_value = 0
    
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            and_value = i & j
            
            if max_value < and_value < K:
                max_value = and_value
            
            if max_value == K - 1:
                return max_value
    
    return max_value

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        count = int(first_multiple_input[0])
        lim = int(first_multiple_input[1])
        res = bitwiseAnd(count, lim)
        fptr.write(str(res) + '\n')
        
    fptr.close()
