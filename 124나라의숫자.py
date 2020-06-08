n = 10

number_list = ['4','1','2']
answer = []
string = ''
while(n>0):
    result_num = n % 3
    if result_num == 0:
        answer.append(number_list[0])
    elif result_num == 1:
        answer.append(number_list[1])
    elif result_num == 2:
        answer.append(number_list[2])
    n = (n-1)//3

string = (''.join(reversed(answer)))
print(string)
"""
1 1
2 2
3 4
4 11
5 12
6 14
7 21
8 22
9 24
10 41
11 42
12 44
13 111
14 112
15 114
16 121
"""
# 배열 선언 0으로 초기화, 길이는 n * 3...? 
# 3번 카운트 후 + 1
# 원소 값이 4인 경우 앞에있는 0을 + 시킴 , 앞에 숫자가 4인 경우에도 마찬가지로 앞에 있는 숫자 +1 시킴? 

