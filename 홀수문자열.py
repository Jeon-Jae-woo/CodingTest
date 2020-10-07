def solution(S):
    answer = 0
    s_dict = {}
    for i in range(0, len(S)):
        if S[i] not in s_dict:
            s_dict[S[i]] = 1
        else:
            s_dict[S[i]] +=1
    

    for key, value in s_dict.items():
        if value%2 == 1:
            answer +=1
    
    return answer




S = "abebeaedeac"

result = solution(S)

print(result)