import sys

n, m, k = map(int, sys.stdin.readline().split(" "))
data = list(map(int, sys.stdin.readline().split(" ")))

data.sort()
first = data[n-1]
second = data[n-2]

count = 0
result = 0
for i in range(0,m):
    count+=1
    if(count>k):
        count=0
        result += second
    else:
        result +=first

print(result)

