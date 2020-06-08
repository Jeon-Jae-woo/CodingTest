import sys

class Queue:
    def __init__(self):
        self.queue = []

    def push(self, number):
        self.queue.append(number)
        return

    def pop(self):
        if not self.queue:
            return -1
        else:
            result = self.queue[0]
            del self.queue[0]
            return result
    
    def size(self):
        return len(self.queue)

    def empty(self):
        if not self.queue:
            return 1
        else:
            return 0

    def front(self):
        if not self.queue:
            return -1
        else:
            return self.queue[0]
    
    def back(self):
        if not self.queue:
            return -1
        else:
            return self.queue[-1]

queue = Queue()
n = int(sys.stdin.readline())

for i in range(0,n):
    string = sys.stdin.readline().rstrip()

    if 'push' in string:
        result = string.split(' ')
        number = int(result[1])
        queue.push(number)
    
    if 'pop' in string:
        pop_result = queue.pop()
        print(pop_result)

    if string in 'size':
        size_result = queue.size()
        print(size_result)

    if string in 'empty':
        empty_result = queue.empty()
        print(empty_result)
    
    if string in 'front':
        front_result = queue.front()
        print(front_result)
    
    if string in 'back':
        back_result = queue.back()
        print(back_result)
        

    
