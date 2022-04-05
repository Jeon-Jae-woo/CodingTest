# 분해합

import sys

n = int(sys.stdin.readline())

for i in range(1,n):
    sum = i
    temp = i
    while temp!=0:
        sum += temp%10
        temp = int(temp/10)
    if sum==n:
        print(i)
        exit()

print(0)

