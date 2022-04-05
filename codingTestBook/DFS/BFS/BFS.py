from collections import deque

def BFS(graph, root):
    visited = []
    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        if node not in visited:
            temp = graph[node]
            temp.sort()
            queue.extend(temp)
            visited.append(node)
    
    return visited

graph = {1: [2, 3, 4], 2: [1, 4], 3: [1, 4], 4: [1, 2, 3]}

result = BFS(graph,1)

print(result)
