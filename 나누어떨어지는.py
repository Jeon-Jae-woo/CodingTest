def solution(arr, divisor):
    answer = []
    for i in range(0,len(arr)):
        if arr[i]%divisor == 0:
            answer.append(arr[i])
    
    if not answer:
        answer.append(-1)

    answer.sort()
    return answer



arr =[3,2,6]
divisor = 10

result = solution(arr,divisor)
print(result)