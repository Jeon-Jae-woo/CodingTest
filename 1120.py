# 문자열 
# 그리디 알고리즘

# for 문으로 A 문자열 반복, B 문자열은 +1씩 해서 반복(단, B 길이를 초과하면 X)
# B를 B len - A len 만큼 ? ???? X 
# A 문자열 앞 뒤 추가는 어차피 결과가 0 이므로 카운트 X

# A 문자열은 계속 반복, B 문자열은 +1 부터 A len 까지 계속 반복해야함
# i + len(A) > len(B)
import sys

A,B = map(str, sys.stdin.readline().strip().split(' '))

min_value = 50
for i in range(0,len(B)):
    if i+len(A) > len(B):
        break
    count = 0
    temp = i
    for j in range(0,len(A)):
        if B[temp] != A[j]:
            count +=1
        temp +=1
    if min_value > count:
        min_value = count

print(min_value)


