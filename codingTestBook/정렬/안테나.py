# 해당 위치로부터 거리의 총 합이 최소가 되는 집 찾기

import sys

N = int(sys.stdin.readline().strip())
house = list(map(int, sys.stdin.readline().strip().split()))
house.sort()
print(house[(N-1)//2])

"""
중간지점이 best
"""