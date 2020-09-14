# 문자열압축

# 최대 문자열 압축 가능은 문자열 길이에서 절반 len/2
# 문자열 1개 넣고 비교? 다르면 pass 같으면 count 
# 다른 경우 해당 문자열로 교체하고 count = 0으로 초기화 하고 시작 문자열 앞에 count 추가


# for 문자열 길이 절반
# for 길이 만큼 해당 문자열 삽입
# for 문자열 전체 반복
#    if eq == s[j:j+i]

# 미완성

def solution(s):
    answer = 0
    cut = int(len(s)/2)
    count = 0
    for i in range(1,cut+1):
        eq = s[:i]
        start_index = 0 # ?? 
        for j in range(i,len(s), i):
            if eq == s[j:j+i]:
                count +=1
            else:
    return answer





s = "aabbaccc"
result = solution(s)

print(int(len(s)/2))