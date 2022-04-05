# 맨 앞이거나 맨 뒤가 아닌 경우 j-1, j 값 비교 후 +
# 맨 앞이거나 맨 뒤인 경우 그대로 j + 시킴

# 정수 삼각형
import sys

triangle = []
n = int(sys.stdin.readline())
for i in range(n):
    line = list(map(int,sys.stdin.readline().split()))
    triangle.append(line)

for i in range(0,len(triangle)):
    if i == 0:
        continue
    for j in range(0,len(triangle[i])):
        if j==0:
            triangle[i][j] += triangle[i-1][j]
        elif j==len(triangle[i])-1:
            triangle[i][j] += triangle[i-1][-1]
        else:
            temp = triangle[i-1][j-1] if triangle[i-1][j-1] > triangle[i-1][j] else triangle[i-1][j]
            triangle[i][j] += temp

print(max(triangle[-1]))