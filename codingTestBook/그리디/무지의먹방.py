# food_times 1 ~ 2000
# food_times 1 ~ 1000이하 자연수


import sys

food_times = list(map(int,sys.stdin.readline().split()))
k = int(sys.stdin.readline())
count = 0
i=0
while True:
    i +=1
    if len(food_times) <= i:
        i=0
    if food_times[i] == 0:
        continue

    food_times[i] -=1
    k -=1
    if k==0:
        break

print(i+1)


