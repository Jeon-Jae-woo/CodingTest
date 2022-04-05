# 높이 H 절단기, 높이가 H보다 긴 떡은 H 위의 부분이 잘리고, 낮은 떡은 잘리지 않음
# 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램
# 이진 탐색 사용

import sys

N,M = map(int, sys.stdin.readline().strip().split())
rice_cake = list(map(int, sys.stdin.readline().strip().split()))

# 떡의 높이
start = 0
end = max(rice_cake)

result_h = 0
while (start <= end):
    total = 0
    mid = (start+end)//2
    for x in rice_cake:
        if x > mid:
            total += x-mid
    
    # 총합이 요구하는 떡의 길이보다 작은 경우 왼쪽 탐색
    if total < M:
        end = mid-1
    else:
        result_h = mid
        start = mid+1

print(result_h)

"""
4 6
19 15 10 17
"""
