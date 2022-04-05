# 2차원 배열의 합

import sys

m,n = map(int, sys.stdin.readline().split(" "))
arr = []
for i in range(0,n-1):
    arr.append(list(map(int, sys.stdin.readline().split(" "))))


count = int(sys.stdin.readline())

for h in range(0,count):
    sum = 0
    i,j,x,y = map(int, sys.stdin.readline().split(" "))

    for k in range(i-1,x):
        for z in range(j-1,y):
            sum += arr[k][z]
    print(sum)
