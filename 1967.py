import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.child = []
        self.weight = None
        self.parent = None

class Tree:
    def __init__(self, data):
        self.root = Node(data)
        self.leaf_list = []
        self.size = 1

    def insert(self, parent, data, weight):
        check_list = []
        check_list.append(self.root)

        while(check_list):
            node = check_list.pop()
            if node.data == parent:
                new_node = Node(data)
                new_node.parent = node
                new_node.weight = weight
                node.child.append(new_node)
                self.size +=1
                break
            else:
                if not node.child:
                    continue
                else:
                    for i in range(0,len(node.child)):
                        check_list.append(node.child[i])
        return


    def find_leaf(self):
        check_list = []
        check_list.append(self.root)
        while(check_list):
            node = check_list.pop()
            if not node.child:
                self.leaf_list.append(node)
            else:
                for i in range(0, len(node.child)):
                    check_list.append(node.child[i])

        print(self.leaf_list)
        return

    def diameter_of_tree(self):
    
        weight_sum = 0
        for i in range(0,len(self.leaf_list)):
            print('for : ', i)
            temp = 0
            visited = []
            check_list = []
            check_list.append(self.leaf_list[i])
            weight_list = []

            while(check_list): 
                node = check_list.pop()
                print(node.data)
                if node in self.leaf_list:
                    temp += node.weight
                    if weight_sum < temp: 
                        weight_sum = temp

                    visited.append(node)
                    if len(visited) == self.size: 
                        break
                    if node.parent in visited: 
                        temp -= node.weight
                    
                    if check_list:
                        continue
                    else:
                        check_list.append(node.parent)
                else: 
                    if node in visited: 
                        if node.parent not in visited:
                            temp += node.weight
                            weight_list.append(node)
                        
                        check_list.append(node.parent)
                        
                    else:
                        if node.parent in visited and node.parent not in weight_list:
                            temp += node.weight
                            weight_list.append(node)

                        count = 0
                        for i in range(0, len(node.child)):
                            if node.child[i] in visited:
                                count +=1
                                continue
                            else:
                                check_list.append(node.child[i])                        
                    
                        if count == len(node.child): 
                            check_list.append(node.parent)
                            visited.append(node)
                            continue
                        else:
                            visited.append(node)
        return temp

tree = Tree(1)

n = int(sys.stdin.readline())

for i in range(0,n-1):
    parent, data, weight = map(int, sys.stdin.readline().split(' '))
    tree.insert(parent, data, weight)

tree.find_leaf()
temp = tree.diameter_of_tree()
print(temp)

