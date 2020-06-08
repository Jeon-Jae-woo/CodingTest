import sys

class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

class Tree:
    def __init__(self, data):
        self.root = Node(data)
        self.size = 0

    def insert(self, p,l,r):
        visit_node = []
        node_list = []
        node_list.append(self.root)
        while(node_list):
            node = node_list.pop()
            if node.data == p:
                new_node_l = Node(l)
                new_node_r = Node(r)
                node.left = new_node_l
                node.right = new_node_r
                new_node_l.parent = node
                new_node_r.parent = node
                break
            else:
                if node.left != None and node.left not in visit_node:
                    node_list.append(node.left)
                elif node.right != None and node.right not in visit_node:
                    node_list.append(node.right)
                else:
                    visit_node.append(node)

        return

    def Preorder(self): # 전위
        pass

    def Inorder(self): # 중위
        pass

    def Postorder(self): # 후위
        pass


n = int(sys.stdin.readline())

tree = Tree('A')

for i in range(0,n):
    p, l, r = map(str, sys.stdin.readline().rstrip().split(' '))
    tree.insert(p,l,r)
    