import sys
input=sys.stdin.readline

n = 5
lost = [1,2,3,4,5]
reserve = [1,2,3,4,5]

# 차집합 사용 ? 
new_lost = list(set(lost) - set(reserve))
new_reserve = list(set(reserve) - set(lost))

for arr in new_reserve:
    if arr-1 in new_lost:
        new_lost.remove(arr-1)
    elif arr+1 in new_lost:
        new_lost.remove(arr+1) 

answer = n-len(new_lost)
print(answer)