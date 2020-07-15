# 이친수 
# 뭐지

import sys

n = int(sys.stdin.readline())
count = 1
for i in range(2,n+1):
    binary = str(format(i,'b'))
    print("binary = ", binary)

    for j in range(1,len(binary)):
        if binary[0] == '0':
            break
        elif binary[j-1] == '1' and binary[j] == '1':
            break
        elif j == len(binary)-1:
            print(binary)
            count +=1

print(count)