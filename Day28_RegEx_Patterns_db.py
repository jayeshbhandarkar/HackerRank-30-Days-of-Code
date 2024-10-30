import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input().strip())
    gmail_users = []

    for N_itr in range(N):
        firstName, emailID = input().rstrip().split()
        
        if re.search(r'@gmail\.com$', emailID):
            gmail_users.append(firstName)
    gmail_users.sort()
    
    for name in gmail_users:
        print(name)
