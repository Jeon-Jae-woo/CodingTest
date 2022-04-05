# N 보드 크기, K 사과
# 사과 1, 뱀 -1

import sys

# 보드
N = int(sys.stdin.readline().strip())
board = [[0 for col in range(0,N)] for row in range(0,N)]

# 사과
k = int(sys.stdin.readline().strip())
apple_list = []
for i in range(0,k):
    apple_list.append(list(map(int, sys.stdin.readline().strip().split())))

# 조작
c = int(sys.stdin.readline().strip())
control = []
for i in range(0,c):
    control.append(list(map(str, sys.stdin.readline().strip().split())))

# 보드에 사과 넣기
for i in range(0,len(apple_list)):
    k,z = apple_list[i]
    board[k][z] = 1

# 게임 시작
board[0][0] = -1
while True:
    
