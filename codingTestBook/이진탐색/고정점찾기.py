# 정렬된 배열이 존재, 배열 인덱스와 해당 인덱스의 값이 같으면 고정점
# log N 시간으로 풀어야함

# mid를 기준으로 arr[mid] > mid 이면 왼쪽, 반대면 오른쪽 탐색 


import sys


def Fixed_Point(array):
    start = 0
    end = n-1
    while start <= end:
        mid = (start+end)//2
        # 고정점이라면 종료
        if array[mid] == mid:
            return mid
        # 왼쪽 탐색
        if array[mid] > mid:
            end = mid-1
        # 오른족 탐색
        else:
            start = mid+1
    return -1

n = int(sys.stdin.readline().strip())
array = list(map(int, sys.stdin.readline().strip().split()))
array.sort()

values = Fixed_Point(array)

print(values)

"""
5
-15 -6 1 3 7

7
-15 -4 2 8 9 13 15

7
-15 -4 3 8 9 13 15

"""






