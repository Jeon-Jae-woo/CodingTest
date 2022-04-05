import sys

class Node:
    def __init__(self,data):
        self.data = data
        self.parent_node = None
        self.left = None
        self.right = None

class Tree:
    def __init__(self, data):
        self.root = Node(data)
        self.node_list = []
        self.node_list.append(data)

    def insert(self, tree_one, tree_two):
        node = self.root
        visit_node = []
        if tree_one in self.node_list:
            new_node = Node(tree_two)
            parent_node_data = tree_one
            self.node_list.append(tree_two)
        else:
            new_node = Node(tree_one)
            parent_node_data = tree_two
            self.node_list.append(tree_one)

        while(1):
            if node.data == parent_node_data:
                if node.left == None:
                    node.left = new_node
                    new_node.parent_node = node
                    break
                else:
                    node.right = new_node
                    new_node.parent_node = node
                    break
            else:   
                if node.left != None and node.left not in visit_node:
                    node = node.left
                elif node.right != None and node.right not in visit_node:
                    node = node.right
                else:
                    visit_node.append(node)
                    node = node.parent_node
        return
    
    def find_tree(self, data):
        node = self.root
        visit_node = []
        while(1):
            if data > n:
                break

            if node.data == data:
                print(node.parent_node.data)
                break
            if node.left != None and node.left not in visit_node:
                node = node.left
            elif node.right != None and node.right not in visit_node:
                node = node.right
            else:
                visit_node.append(node)
                node = node.parent_node
            
        return

n = int(sys.stdin.readline().rstrip())
tree = Tree(1)
for i in range(0,n-1):
    tree_one, tree_two = map(int, sys.stdin.readline().split(' '))
    tree.insert(tree_one, tree_two)

for i in range(2,n+1):
    tree.find_tree(i)