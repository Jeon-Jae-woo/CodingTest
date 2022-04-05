import sys

class Printer():
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.queue = {}
        self.count = 0

    def important(self):
        import_number = sys.stdin.readline().rstrip().split(' ')
        import_number = list(map(int, import_number))
        for i in range(0,n):
            self.queue[i] = import_number[i]
        if len(import_number) > self.n:
            exit()
        return

    def findLocal(self):
        for key, value in self.queue.items():
            max_value = max(self.queue.values())
            if max_value == value:
                self.count +=1
                if self.m == key:
                    return self.count
                else:
                    del self.queue[key]
                    return self.findLocal()
            else:
                del self.queue[key]
                self.queue.setdefault(key,value)
                return self.findLocal()

test_case = int(sys.stdin.readline())

for i in range(0,test_case):
    n, m = map(int, sys.stdin.readline().rstrip().split(' '))
    printer = Printer(n,m)

    printer.important()
    count = printer.findLocal()
    print(count)
