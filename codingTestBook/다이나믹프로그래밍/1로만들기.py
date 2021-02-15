# 정수 X가 주어질 때 연산은 4가지 가능
# 2,3,5로 나누어 떨어지면 2,3,5로 나눔, x에 1을뺀다

import sys

x = int(sys.stdin.readline().strip())

dx = [0]*30001

for i in range(2,x+1):
    # 1빼기 연산
    dx[i] = dx[i-1]+1
    # 2나누기 연산
    if i % 2 == 0:
        dx[i] = min(dx[i], dx[i//2]+1)
    # 3나누기 연산
    if i % 3 == 0:
        dx[i] = min(dx[i], dx[i//3]+1)
    # 5나누기 연산
    if i % 5 == 0:
        dx[i] = min(dx[i], dx[i//5]+1)

print(dx[x])
