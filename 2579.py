# 계단 오르기

# dp, stair 2배열 필요
# dp는 올라온 계단의 max 값
# stair는 계단의 값

import sys

n = int(sys.stdin.readline())
stair = []
max_list = []

for i in range(n):
    stair.append(int(sys.stdin.readline()))

max_list.append(stair[0])
if n==1:
    print(max_list[-1])
    exit()
max_list.append(max(stair[0], stair[0]+stair[1]))
if n==2:
    print(max_list[-1])
    exit()
max_list.append(max(max_list[0]+stair[2], stair[1]+stair[2]))
if n==3:
    print(max_list[-1])
    exit()
for i in range(3,n):
    max_list.append(max(max_list[i-3]+stair[i]+stair[i-1], max_list[i-2]+stair[i]))
print(max_list[-1])