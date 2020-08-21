# 바이러스

import sys
from collections import deque

def covid_bfs():
    visit = []
    queue = deque()
    queue.append(1)
    while queue:
        node = queue.popleft()
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])
    
    return len(visit)-1


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = {}
for i in range(1,n+1):
    graph[i] = list()

for i in range(0,m):
    a,b = map(int, sys.stdin.readline().split(' '))
    graph[a].append(b)
    if a not in graph[b]:
        graph[b].append(a)

result = covid_bfs()
print(result)