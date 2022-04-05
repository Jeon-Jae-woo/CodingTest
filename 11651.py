import sys
"""
n = int(sys.stdin.readline())
sort_list = []

for i in range(0,n):
    sort_list.append(tuple(map(int, sys.stdin.readline().rstrip().split(' '))))

sort_list.sort()

for i in range(0, len(sort_list)):
    min = i
    for j in range(i+1, len(sort_list)):
        if sort_list[j][1] < sort_list[min][1]:
            min = j
    temp = sort_list[i]
    sort_list[i] = sort_list[min]
    sort_list[min] = temp

for i in range(0, len(sort_list)):
    print(sort_list[i][0], sort_list[i][1])
"""

n = int(sys.stdin.readline())
sort_list = []

for i in range(0,n):
    sort_list.append(tuple(map(int, sys.stdin.readline().split(' '))))

sort_list.sort(key=lambda x: (x[1], x[0]))

for i in range(0, len(sort_list)):
    print(sort_list[i][0], sort_list[i][1])

