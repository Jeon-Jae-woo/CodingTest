


# ㅁ ((( ㅁ ㅁ )( ㅁ ) ㅁ ))( ㅁ )
arrangement = "()(((()())(())()))(())"

new_string = arrangement.replace('()','a')

iron_bar = 0
laser = 0
count = 0
total_laser = 0
for i in range(0, len(new_string)):
    if new_string[i] == '(':
        iron_bar +=1
    if new_string[i] == 'a':
        count += iron_bar
        total_laser +=1
    if new_string[i] == ')':
        iron_bar -=1
        count +=1
       

print(count)

# 레이저를 특정 문자로 교체 시킴
# ( 기호가 나온 경우 판 +1
# ㅁ 카운트 시작
# ) 기호가 나오면 레이저 수 * 판 수 -- 레이저가 하나인 경우 * 2

# 판이 2 이상이면 결과에 - 레이저 ? 

# ((( 3개 ㅁ 갯수 제곱 ? = 9개  
# (((  ㅁ 1개 = 6개
# ((  2개 ㅁ 1개 = 4개 
# 판이 하나인 경우 그냥 반으로 자름
# 판이 여러개 쌓여 있는 경우 count 후 판 갯수 - 시킴 ? 
"""
def solution(arrangement):
    new_string = arrangement.replace('()','a')
    iron_bar = 0
    laser = 0
    count = 0
    total_laser = 0
    answer=0
    for i in range(0, len(new_string)):
        if new_string[i] == '(':
            iron_bar +=1
        if new_string[i] == 'a' and iron_bar >= 1:
            if iron_bar == 1:
                laser +=1
            else:
                laser +=1
                total_laser +=1
    
        if new_string[i] == ')':
            if laser==0:
                iron_bar -=1
                pass
            elif iron_bar == 1 or laser == 1:
                count += (iron_bar *2)
                iron_bar -=1
                laser = 0
            else:
                count += (iron_bar**laser)
                laser=0
                iron_bar -=1
    answer = count - total_laser
    return answer
"""