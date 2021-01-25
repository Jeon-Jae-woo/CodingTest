# 문자열 최대 압축은 문자열 길이의 절반까지 가능
import sys

string = sys.stdin.readline().strip()
result = len(string)
for i in range(1,len(string)//2+1):
    temp = string[0:i]
    temp_string = ''
    count = 1
    for j in range(i,len(string),i):
        if temp == string[j:j+i]:
            count +=1
        else:
            if count > 1:
                temp_string += str(count)+temp
            else:
                temp_string += temp
            
            temp = string[j:j+i]
            count = 1
    
    if count > 1:
        temp_string += str(count)+temp
    else:
        temp_string += temp
        
    result = min(result, len(temp_string))


print(result)