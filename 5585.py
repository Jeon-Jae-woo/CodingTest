# 거스름돈
# 50엔, 10엔, 5엔, 1엔
import sys
pay = 1000

n = int(sys.stdin.readline())
pay -=n

count = 0
while pay!=0:
    if pay >= 500:
        pay -=500
    elif pay >=100:
        pay -=100
    elif pay >=50:
        pay -=50
    elif pay >=10:
        pay -=10
    elif pay >=5:
        pay -=5
    elif pay >=1:
        pay -=1
    count +=1

print(count)

    