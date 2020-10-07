# 히스토그램
# 두 막대중에 더 작은값 두고, 막대 사이에 값을 작은값으로 바꾸고 더하면 끝?
from itertools import permutations



def solution(historgram):
    result_value = 0
    for i in range(0,len(historgram)-2):
        temp = i+2
        count = 0
        for j in range(temp,len(historgram)):
            if historgram[i] > historgram[j]:
                min_value = historgram[j]
            else:
                min_value = historgram[i]
            count +=1
            result = count*min_value

            if result_value < result:
                result_value = result

    print(result_value)




historgram = [2,2,2,3]
#historgram = [6,5,7,3,4,2]

solution(historgram)

a = list(permutations(historgram,2))
print(a)

"""
def solution(histogram):
    dot=[]
    result = 0 
    for i in range(len(histogram)):
        dot+= [[i,histogram[i]]]
        
    for i in range(len(dot)):
        for k in range(i+1, len(dot)):
            x=dot[k][0]- dot[i][0]-1
            y=min([dot[k][1],dot[i][1]])
            result = max(result,x*y)
            
    
    return result
"""