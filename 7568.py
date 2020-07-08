# 덩치

"""
A	<55, 185>	2
B	<58, 183>	2
C	<88, 186>	1
D	<60, 175>	2
E	<46, 155>	5
"""
# 자신보다 크면 count +1
# 딕셔너리 값 으로 비교 ? 

import sys

class Person():
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
        self.rank = 0

n = int(sys.stdin.readline())
per_list = []
for i in range(0,n):
    key, value = map(int,sys.stdin.readline().split())
    per_list.append(Person(key,value))

rank_list = []
for i in range(0,n):
    count = 1
    for j in range(0,n):
        if i == j:
            continue
        else:
            if per_list[i].weight < per_list[j].weight and per_list[i].height < per_list[j].height:
                count +=1
            else:
                pass
    per_list[i].rank = count
    rank_list.append(str(per_list[i].rank))

print(' '.join(rank_list))