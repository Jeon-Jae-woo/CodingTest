# 한 줄로 서기
# 2차원 배열 선언 [키, 앞에 큰 사람 카운트]
# 0은 무조건 붙이고 시작? 

import sys

n = int(sys.stdin.readline())
h = list(map(int, sys.stdin.readline().split(' ')))
seq = [0 for i in range(n)]
person = [[0 for i in range(2)] for row in range(0,n)]

for i in range(0,n):
    person[i][0] = i+1
    person[i][1] = h[i]

person.sort(key=lambda x: (x[1], x[0]))

seq[0] = person[0][0]
for i in range(1,n):
    count = 0
    for j in range(0,i+1):
        if i == n:
            continue
        if count == person[i][1]:
            if seq[j] == 0:
                seq[j+1] = seq[j]
                seq[j] = person[i][0]
            else:
                seq[j] = person[i][0]
        elif person[j][0] > person[i][0]:
            count +=1

print(seq)


# 실패

