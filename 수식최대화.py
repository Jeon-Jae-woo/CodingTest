# 수식 최대화
import copy
import re

def solution(expression):
    exp = ['+','-','*','+','*','-','-','+','*','-','*','+','*','+','-','*','-','+'] # 수식 모든 조합
    answer = 0
    count = 0
    expressionList = re.split(r'(\D)',expression)
    temp_list = copy.deepcopy(expressionList)

    for i in range(0,len(exp)):
        j=0
        if i%3==0 and i !=0:
            temp_list = copy.deepcopy(expressionList)
        while True:
            if exp[i] == temp_list[j]:
                if exp[i]=="*":
                    temp = int(temp_list[j-1])*int(temp_list[j+1])
                    temp_list[j] = temp
                    del temp_list[j-1], temp_list[j]
                    j=0
                    continue
                elif exp[i] == "+":
                    temp = int(temp_list[j-1])+int(temp_list[j+1])
                    temp_list[j] = temp
                    del temp_list[j-1], temp_list[j]
                    j=0
                    continue
                elif exp[i] == "-":
                    temp = int(temp_list[j-1])-int(temp_list[j+1])
                    temp_list[j] = temp
                    del temp_list[j-1], temp_list[j]
                    j=0
                    continue
                else:
                    j +=1
            else:
                j +=1
            
            if j>=len(temp_list)-1:
                break
        if len(temp_list) == 1:
            value = abs(int(temp_list[0]))
            if answer < value:
                answer = value

    return answer



expression = "100-200*300-500+20"
# "50*6-3*2"
#expression = ['100','-','200','*','300','-','500','+','20']
#expression = ['50','*','6','-','3','*','2']

result = solution(expression)

print(result)
