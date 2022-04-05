# 9012
import sys

n = int(sys.stdin.readline())

count = 0
for i in range (0, n):
    string = sys.stdin.readline().rstrip()
    
    if 2>len(string) or 50<len(string):
        exit() 

    if len(string)%2 == 1:
        print('NO')
        continue

    for j in range(0, len(string)):
        if string[j] == '(':
            count +=1
        if string[j] == ')':
            count -=1        
        if count == -1:
            print('NO')
            break
        if j == len(string)-1:
            if count == 0:
                print('YES')
            else:
                print('NO')
    count=0

