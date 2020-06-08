import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
        self.result = []
        self.cur = Node('cur') # 커서 노드

    def insert(self, data):
        node = self.head
        while(1):
            if node.next == None:
                break
            node = node.next
        
        new_Node = Node(data)
        new_Node.prev = node
        node.next = new_Node
        self.cur.prev = new_Node
        return

    def L(self):
        if self.cur.prev == None:
            return
        self.cur.next = self.cur.prev
        self.cur.prev = self.cur.prev.prev
        return

    def D(self):
        if self.cur.next == None:
            return
        self.cur.prev = self.cur.next
        self.cur.next = self.cur.prev.next
        return

    def B(self):
        if self.cur.prev == None:
            return
        
        del_node = self.cur.prev # 삭제할 노드 (커서의 왼쪽 노드)
        if del_node.next == None: # 삭제할 노드가 맨 마지막인 경우
            del_node.prev.next = None
            self.cur.prev = del_node.prev
            del del_node
        elif del_node.prev == None: # 삭제할 노드가 첫번째인 경우
            del_node.next.prev = None
            self.head = del_node.next
            self.cur.prev = None
            del del_node
        else: # 중간에 위치하는 경우
            del_node.prev.next = del_node.next
            del_node.next.prev = del_node.prev
            self.cur.prev = del_node.prev
            del del_node
        return


    def P(self, s):
        new_node = Node(s)
        if self.cur.next == None: # 마지막 
            new_node.prev = self.cur.prev
            self.cur.prev.next = new_node
            self.cur.prev = new_node
        elif self.cur.prev == None: # 맨 앞인 경우
            self.head = new_node
            new_node.next = self.cur.next
            self.cur.next.prev = new_node
            self.cur.prev = new_node
        else: # 중간 
            new_node.prev = self.cur.prev
            new_node.next = self.cur.next
            self.cur.prev.next = new_node
            self.cur.next.prev = new_node
            self.cur.prev = new_node
        return

    def findList(self):
        head = self.head
        result = []
        while(1):
            if head.next == None:
                result.append(head.data)
                return result
            else:
                result.append(head.data)
                head = head.next
        return


string = sys.stdin.readline().rstrip().lower()
n = int(sys.stdin.readline())

linkedList = LinkedList(string[0])
result = []
for i in range(1,len(string)):
    linkedList.insert(string[i])    

for i in range(0,n):
    command = sys.stdin.readline().rstrip()

    if 'L' in command:
        linkedList.L()
        
    if 'D' in command:
        linkedList.D()
        
    if 'B' in command:
        linkedList.B()
       
    if 'P' in command:
        command = command.split(' ')
        linkedList.P(command[1])
        
result = linkedList.findList()
print(''.join(result))


