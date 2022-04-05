# 국어 낮은 점수로
# 국어 같으면 영어 높은 점수로
# 국어 영어 같으면 수학 점수가 낮은 순서로
# 국영수가 같으면 이름이 증가하는 순서로 정렬

import sys

N = int(sys.stdin.readline().strip())

students = []
for i in range(0,N):
    students.append(sys.stdin.readline().strip().split())

students.sort(key= lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
    print(student[0])


"""
12
Junkyu 50 60 100
SangKeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90
"""