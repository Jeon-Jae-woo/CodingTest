import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self, data):
        node = Node(data)
        self.head = node # 첫번째 노드
        self.size = 1
        self.string = '<'

    def insert(self, data):
        node = self.head
        while(1):
            if node.next == None:
                break
            node = node.next
        new_node = Node(data)
        node.next = new_node
        new_node.prev = node
        self.size +=1
        return

    def delete(self, m):
        now_node = self.head
        while(1):
            if self.size==1:
                temp = now_node.data
                self.string = self.string + str(temp) + '>'
                del now_node
                break # size가 1이면 종료

            for i in range(0,m-1):
                if now_node.next == None:
                    now_node = self.head 
                else:   
                    now_node = now_node.next

            now_node = self.deleteNode(now_node)  

        return self.string

    def deleteNode(self, node):
        if node == self.head: # 첫번째 노드
            next_node = node.next
            next_node.prev = None
            self.string = self.string + str(node.data) + ', '
            del node
            self.head = next_node
            self.size -=1
            return next_node
        elif node.next is None: # 맨 마지막 노드
            prev_node = node.prev
            prev_node.next = None
            self.string = self.string + str(node.data) + ', '
            del node
            self.size -=1
            return self.head
        else:
            next_node = node.next
            prev_node = node.prev
            self.string = self.string + str(node.data) + ', '
            del node
            next_node.prev = prev_node
            prev_node.next = next_node
            self.size -=1
            return next_node
            

n, m = map(int, sys.stdin.readline().rstrip().split(' '))

result_list = []
list = LinkedList(1)
for i in range(2,n+1):
    list.insert(i)

result_list = list.delete(m)

print(result_list)