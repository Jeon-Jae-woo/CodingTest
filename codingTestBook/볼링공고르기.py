# 볼링공 고르기
# 배열 모든 조합 구하기, but 조합하는 숫자가 같은 경우 제외

#bol = [1,3,2,3,2]
#bol = [1,5,4,3,2,4,5,2]

import sys

n, m = map(int, sys.stdin.readline().split(' '))
bol = list(map(int, sys.stdin.readline().split(' ')))

count = 0
for i in range(0,len(bol)):
    for j in range(i,len(bol)):
        if bol[i] == bol[j]:
            continue
        else:
            count +=1

print(count)
