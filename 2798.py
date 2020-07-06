# 블랙잭
# 3개 조합 배열 순회

import sys

n, m = map(int,sys.stdin.readline().split())
card = list(map(int,sys.stdin.readline().split()))

max_value = 0
for i in range(0,n):
    for j in range(i+1,n):
        for z in range(j+1,n):
            temp = card[i] + card[j] + card[z]
            if temp > max_value and temp <= m:
                max_value = temp

print(max_value)
                 