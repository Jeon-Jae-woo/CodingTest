# DFS 스택 사용

def DFS(graph, root):
    visited = []
    stack = [root]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            temp = graph[node]
            temp.sort(reverse=True)
            stack.extend(temp)
            

    return visited

graph = {1: [2, 3, 4], 2: [1, 4], 3: [1, 4], 4: [1, 2, 3]}

result = DFS(graph,1)

print(result)