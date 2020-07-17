# 파도반 수열
# list[i] = list[i-2] + list[i-3]

import sys

shapes = [1,1,1]

for j in range(3,101):
    shapes.append(shapes[j-2]+shapes[j-3])


n = int(sys.stdin.readline())
for i in range(0,n):
    m = int(sys.stdin.readline())
    print(shapes[m-1])