import sys

n = int(sys.stdin.readline())
number = []
result = []
temp = ''
for i in range(n):
    string = sys.stdin.readline().rstrip()

    for j in range(len(string)):
        if string[j] in '1234567890':
           temp += string[j]
           if j == len(string)-1:
               number.append(temp)
               temp = ''
        else:
            number.append(temp)
            temp = ''  
print(number)
for i in range(len(number)):
    string2 = number[i]
    if '0' in string2 and len(string2) > 1:
        result.append(int(string2.lstrip('0')))
    elif string2 != '':
        result.append(int(string2))

result.sort()
for i in range(len(result)):
    print(result[i])
