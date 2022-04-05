# 10818
import sys
n = int(sys.stdin.readline())
if n<1 or n>10000:
    exit()
stack = []
for i in range(0, n):
    string = sys.stdin.readline()
    if 'push' in string:
        result = string.split(' ')
        number = int(result[1])
        if number<1 or number>100000:
            exit()
        stack.append(number)
    if 'pop' in string:
        if not stack:
            print(-1)
        else:
            pop_result = stack.pop()
            print(pop_result)
    if 'size' in string:
        print(len(stack))
    if 'empty' in string:
        if not stack:
            print(1)
        else:
            print(0)
    if 'top' in string:
        if not stack:
            print(-1)
        else:
            print(stack[-1])