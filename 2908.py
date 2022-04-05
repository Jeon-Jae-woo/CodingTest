# 2908
A, B = input().split(' ')

# 0 검사
string = A+B
if '0' in string:
    exit()

# int 변환
number = int(''.join(reversed(A)))
number2 = int(''.join(reversed(B)))

# 조건
if number==number2 or number<100 or number2<100:
    exit()
elif number>number2:
    print(number)
else:
    print(number2)

