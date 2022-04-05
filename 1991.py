import sys

class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

class Tree:
    def __init__(self, data):
        self.root = Node(data)
        self.check = ''        

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
                break
            else:
                if node.left != None and node.left:
                    node_list.append(node.left)
                if node.right != None and node.right:
                    node_list.append(node.right)
    
        return

    def Preorder(self): # 전위 / root - left - right
        string = ''
        node_list = []
        node_list.append(self.root)
        while(node_list):
            node = node_list.pop()
            string = string + node.data
            if node.right != None:
                if node.right.data != '.':
                    node_list.append(node.right)
            if node.left !=None:
                if node.left.data != '.':
                    node_list.append(node.left)
        
        return string
                

    def Inorder(self): # 중위 / left - root - right
        string = ''
        node_list = []
        visit_node = []
        node_list.append(self.root)
        node = self.root
        while(node_list):
            if node.left != None and (node.left.data !='.' and node.left not in visit_node):
                node_list.append(node.left)
                node = node.left
            else:
                node = node_list.pop()
                string = string + node.data
                visit_node.append(node)
                
                if node.right != None:
                    if node.right.data != '.' and node.right not in visit_node:
                        node_list.append(node.right)
                        node = node.right
        return string

    def Postorder(self): # 후위
        string = ''
        visit_node = []
        node_list = []
        node_list.append(self.root)
        while(node_list):
            if node_list[-1].left != None and (node_list[-1].left.data != '.' 
            and node_list[-1].left not in visit_node):    
                node_list.append(node_list[-1].left)
            else:
                if node_list[-1].right != None and (node_list[-1].right.data != '.' 
                and node_list[-1].right not in visit_node):
                    node_list.append(node_list[-1].right)
                else:
                    node = node_list.pop()    
                    string = string + node.data
                    visit_node.append(node)
        return string

n = int(sys.stdin.readline())
tree = Tree('A')
for i in range(0,n):
    p, l, r = map(str, sys.stdin.readline().rstrip().split(' '))
    tree.insert(p,l,r)

string = tree.Preorder()
string2 = tree.Inorder()
string3 = tree.Postorder()
print(string)
print(string2)
print(string3)

