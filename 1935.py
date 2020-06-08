# 1935 
import sys
import re
# 실패
def calc(oper, stack):
    second = stack.pop()
    first = stack.pop()
    if oper == '+':
        result = first + second
        stack.append(result)
    elif oper == '-':
        result = first - second
        stack.append(result)
    elif oper == '*':
        result = first * second
        stack.append(result)
    elif oper == '/':
        result = first / second
        stack.append(result)
    else:
        exit()
    return


# 대문자 숫자로 변환 X 
n = int(sys.stdin.readline())
string = str(sys.stdin.readline().rstrip()) # ABC*+DE/-

# 무쓸모 ; 
number = []
for i in range(0,n):
    number.append(int(input()))


stack = []

for i in range(0, len(string)):
    if string[i] in '+-*/':
        calc(string[i], stack)
    else:
        stack.append(int(string[i]))


print(stack.pop())




