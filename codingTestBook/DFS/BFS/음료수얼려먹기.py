# N, M
import sys

def Ice(x,y):
    if x <= -1 or x >= N or y <=-1 or y >=M:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
            
        Ice(x-1,y)
        Ice(x+1,y)
        Ice(x,y-1)
        Ice(x,y+1)

        return True
    
    return False


N,M = map(int, sys.stdin.readline().strip().split())
graph = []
for i in range(0,N):
    graph.append(list(map(int,sys.stdin.readline().strip())))
count = 0
for i in range(0,N):
    for j in range(0,M):
        if Ice(i,j) == True:
            count +=1

print(count)


"""
비어있는(0인 경우)에 해당 위치를 기준으로 DFS탐색을 하고 재귀 함수를 통해서 4가지 방향을 확인한다.
벽을 만나거나 크기에 맞지 않을때까지 탐색을 하고 값을 1로 갱신한 후 종료한다
"""