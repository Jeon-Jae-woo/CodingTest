# 1은 길, 0은 괴물
# BFS사용
# 괴물을 피해 미로 탈출구에 도착하는 문제(탈출구는 배열의 마지막)
# 최단 경로 구하기
import sys
from collections import deque

def Maze(x,y):
    # 상하좌우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(0,4):
            nx = x+dx[i]
            ny = y+dy[i]
            # 범위를 벗어난 경우
            if nx <= -1 or nx >= n or ny <= -1 or ny >=m:
                continue
            # 괴물을 만난 경우
            if graph[nx][ny] == 0:
                continue
            # 탐색하지 않은 경로에 대해서만 갱신
            if graph[nx][ny] == 1:
                queue.append((nx,ny))
                graph[nx][ny] = graph[x][y]+1
    
    return graph[n-1][m-1]


n, m = map(int, sys.stdin.readline().strip().split())

graph = []
for i in range(0,n):
    graph.append(list(map(int, sys.stdin.readline().strip())))


result = Maze(0,0)
print(result)

"""
5 6
101010
111111
000001
111111
111111
"""

"""
1,1 시작지점부터 bfs를 사용하여 거리를 갱신하며 출구까지 탐색
방문하지 않은 노드가 있다면 해당 노드를 기준으로 상,하,좌,우를 탐색하고 거리를 갱신
"""
