# N * N 의 사각형
# (1,1) 부터 시작
# L R U D 으로 이동 가능

import sys

N = int(sys.stdin.readline())
move = list(map(str, sys.stdin.readline().split()))
point = [1,1]

for m in move:
    if m=="U" or m=="D":
        temp = point[0]
        if m=="U":
            temp -=1
        elif m=="D":
            temp +=1

        if temp != 0 and temp != N:
            point[0] = temp

    elif m=="L" or m=="R":
        temp = point[1]
        if m=="L":
            temp -=1
        elif m=="R":
            temp +=1
        
        if temp !=0 and temp != N:
            point[1] = temp


print(point)