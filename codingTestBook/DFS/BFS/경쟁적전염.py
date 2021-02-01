import sys
from collections import deque

n, k = map(int, sys.stdin.readline().strip().split())
board = []
virus = []
for i in range(0,n):
    board.append(list(map(int, sys.stdin.readline().strip().split())))
    # 바이러스의 정보를 저장
    for j in range(0,n):
        if board[i][j] != 0:
            virus.append([board[i][j],0,i,j])
virus.sort()
queue = deque()
queue.extend(virus)

# 초, 좌표
S,X,Y = map(int,sys.stdin.readline().strip().split())

# 상하좌우
dx = [-1,0,1,0]
dy = [0,-1,0,1]


#바이러스 전염 시작
while queue:
    virus_type, temp_s, temp_x, temp_y = queue.popleft()
    if S == temp_s:
        break
    for i in range(0,4):
        nx = dx[i] + temp_x
        ny = dy[i] + temp_y
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            if board[nx][ny] == 0:
                board[nx][ny] = virus_type
                queue.append([virus_type, temp_s+1,nx,ny])
                

print(board[X-1][Y-1])


"""
3 3
1 0 2
0 0 0
3 0 0
2 3 2
"""


"""
바이러스는 작은 순서로 전염이 진행되야 하므로 별도의 바이러스 배열을 만들고 sort를 사용해서 큐에 넣었다
바이러스가 작은 순서대로 BFS를 사용해서 값을 갱신, 큐에는 바이러스에 대한 정보가 필요하고, 몇 초가 지난 시점에서의
borad가 필요하므로 s+1로 초를 계산, 좌표와 같이 큐에 넣는다.
"""
