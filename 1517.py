import sys

n = int(sys.stdin.readline())
arr = list(map(int, input().split()))
if n < len(arr):
    exit()

temp = 0
count = 0
for i in range(len(arr)-1,0,-1):
    for j in range(0,i):
        if arr[j] > arr[j+1]:
            count +=1
            temp = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = temp
print(count)



