# BFS와 DFS

import sys
from collections import deque
import copy

def BFS(graph, start_node):
    bfs_graph = copy.deepcopy(graph)
    visit = []
    queue = deque()
    queue.append(start_node)
    while queue:
        node = queue.popleft()
        if node not in visit:
            temp_list = bfs_graph[node]
            temp_list.sort()
            visit.append(node)
            queue.extend(bfs_graph[node])

    return visit

def DFS(graph, start_node):
    dfs_graph = copy.deepcopy(graph)
    visit = []
    stack = [start_node]
    
    while stack:
        node = stack.pop()
        if node not in visit:
            temp_list = dfs_graph[node]
            temp_list.sort(reverse=True)
            visit.append(node)
            stack.extend(temp_list)

    return visit

graph = {}
n,m,v = map(int,sys.stdin.readline().split(' '))

for i in range(1,n+1):
    graph[i]= list()

for i in range(0,m):
    a,b = map(int, sys.stdin.readline().split(' '))
    graph[a].append(b)
    if a not in graph[b]:
        graph[b].append(a)

result = DFS(graph,v)

#string = " ".join(str(i) for i in result)
print(*result)

result = BFS(graph,v)
string = " ".join(str(i) for i in result)
print(string)


