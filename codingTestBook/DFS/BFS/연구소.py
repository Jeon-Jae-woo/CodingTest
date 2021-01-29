# 지도의 크기가 최대 8이므로 시간 초과는 없음
# 벽을 3개를 세우고 바이러스(2)를 기준으로 DFS를 실행하며 0인 경우 스택에 넣고 2로 바꾸고 1인 경우는 패스

import sys

n,m = map(int, sys.stdin.readline().strip().split())
graph = []
for i in range(0,n):
    graph.append(list(map(int, sys.stdin.readline().strip().split())))
temp = [[0 for _ in range(0,m)] for _ in range(0,n)]

# 안전지대 계산
def check_score():
    value = 0
    for i in range(0,n):
        for j in range(0,m):
            if temp[i][j] == 0:
                value +=1
    return value

# 바이러스가 퍼지는 동작
def virus_dfs(x,y):
    dx = [-1,0,-1,0]
    dy = [0,1,0,1]

    for i in range(0,4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >=0 and nx < n and ny >=0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus_dfs(nx,ny)
    return

def dfs(count):
    global result
    if count ==3:
        # 임시 배열에 그래프 값을 넣는다
        for i in range(0,n):
            for j in range(0,m):
                temp[i][j] = graph[i][j]

        # 바이러스 칸인 경우에 번지기 시작
        for i in range(0,n):
            for j in range(0,m):
                if temp[i][j] == 2:
                    virus_dfs(i,j)
        
        result = max(result, check_score())
        return

    for i in range(0,n):
        for j in range(0,m):
            if graph[i][j] == 0:
                graph[i][j]=1
                count +=1
                dfs(count)
                count -=1
                graph[i][j]=0
    
    return

dfs(0)
print(result)


"""
7 7
2 1 0 0 1 1 2
1 0 1 0 1 2 2
0 1 1 0 1 2 2
0 1 0 0 0 1 2
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
"""