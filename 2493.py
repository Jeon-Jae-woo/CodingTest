# 2493
import sys

n = int(sys.stdin.readline())
top_list = list(map(int, sys.stdin.readline().split(' '))) # 6 9 5 7 4

if n < len(top_list) or max(top_list) > 100000000:
    exit()
top_dict = {}
for i in range(0,n):
    top_dict[top_list[i]] = i+1

result = []
stack= []
for i in range(0,len(top_list)):
    if not stack:
        stack.append(top_list[i])
        result.append('0')
        continue

    while(stack):
        if stack[-1] < top_list[i]:
            stack.pop()
            if not stack:
                result.append('0')
                stack.append(top_list[i])
                break
        else:
            result.append(str(top_dict[stack[-1]]))
            stack.append(top_list[i])
            break

print(' '.join(result))
