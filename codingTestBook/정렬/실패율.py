# 실패율 = 해당 스테이지에서 실패한 인원/ 클리어 인원
# 계수 정렬 사용?
# 스테이지가 더 남아있지만 사람이 없는 경우도 생각

def solution(N, stages):
    answer = []
    temp_stages = [0]*(max(stages)+1)
    for i in range(len(stages)):
        temp_stages[stages[i]] +=1
    
    total_person = len(stages)
    fail = []
    for i in range(1,N+1):
        if total_person==0:
            fail.append([i,0])
        else:
            fail.append([i,temp_stages[i]/total_person])
            total_person -= temp_stages[i]
    
    fail.sort(key=lambda x: x[1], reverse=True)
    
    for i in range(0,N):
        answer.append(fail[i][0])
    return answer

"""
배열을 하나 더 선언하고 스테이지에 있는 인원을 카운트
해당 스테이지 실패율을 계산하고 실패율 배열에 추가 및 총 인원수 감소(스테이지에서 실패한 사람은 다음 스테이지에 못감)
해당 스테이지에 아무도 성공하지 못했다면 실패율은 0
실패율이 높은 순서대로 정렬하고 반환
"""


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]	

#N = 4
#stages = [4,4,4,4,4]
valuess = solution(N,stages)

print(valuess)
