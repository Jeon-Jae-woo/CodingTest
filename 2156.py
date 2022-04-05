# 포도주시식

# dp, stair 2배열 필요

import sys

n = int(sys.stdin.readline())
wine = []
max_list = []

for i in range(n):
    wine.append(int(sys.stdin.readline()))

max_list.append(wine[0])
if n==1:
    print(max_list[-1])
    exit()
max_list.append(max(wine[0], wine[0]+wine[1]))
if n==2:
    print(max_list[-1])
    exit()
temp = max(max_list[0]+wine[2], wine[1]+wine[2])
max_list.append(max(temp,max_list[1]))
if n==3:
    print(max_list[-1])
    exit()
for i in range(3,n):
    temp =max(max_list[i-3]+wine[i]+wine[i-1], max_list[i-2]+wine[i])
    max_list.append(max(temp,max_list[i-1]))
print(max_list[-1])
