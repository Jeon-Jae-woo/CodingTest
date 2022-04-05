# 특정 거리의 도시가 몇 개가 있는지 확인하는 문제
# n 도시, m 도로, k 특정 거리, x 시작 도시
# 도시를 -1로 초기화 -> 시작 도시는 0



import sys
from collections import deque

"""
n,m,k,x = map(int,sys.stdin.readline().strip().split())
graph = [[]for _ in range(0,n+1)]

for _ in range(0,m):
    a,b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)

distance = [-1] *(n+1)
distance[x] = 0

q = deque([x])

while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now]+1
            q.append(next_node)
    

check = False
for i in range(1,n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)
"""

"""
4 4 2 1
1 2
1 3
2 3
2 4
"""

n,m,k,x = map(int, sys.stdin.readline().strip().split())

graph = [[]for i in range(0,n+1)]

for i in range(0,m):
    a,b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)

# 거리 초기화
distance = [-1] *(n+1)
distance[x] = 0

queue = deque([x])

while queue:
    node = queue.popleft()
    for node_list in graph[node]:
        if distance[node_list] == -1:
            distance[node_list] = distance[node]+1
            queue.append(node_list)
        

k_check = False
for i in range(0,len(distance)):
    if distance[i] == k:
        print(i)
        k_check = True
if k_check == False:
    print(-1)
