# key는 4번 회전 가능
# key는 0,M ~ 0,M 까지 채우기
# lock, key 최대 판을 3배로 설정
# lock 는 중앙 부분에 넣기 -> how???? 
# key는 lock보다 작다

# key는 4방향 회전이 가능
# 회전 전의 열 번호와 회전 후의 행 번호가 일치한다
# 회전 후의 열은 N-1 에서 회전 전의 행 값을 뺀 값과 같다 (N은 배열의 행과 열의 크기?)
def rotation(rotation_key, m):
    temp_list = [[0 for col in range(m)] for row in range(m)]
    for i in range(0,m):
        for j in range(0,m):
            temp_list[j][m-1-i] = rotation_key[i][j]
    return temp_list

# 자물쇠가 모두 1인지 체크
def lock_check(array, n):
    for x in range(n,n+n):
        for y in range(n,n+n):
            if array[x][y] != 1:
                return False
    return True
        

def solution(key, lock):
    n = len(lock)
    m = len(key)
    array = [[0 for col in range(n*3)] for row in range(n*3)]
    answer = False
    # lock을 큰 판 중앙에 넣음
    lock_i = -1
    for i in range(n,n+n):
        lock_i +=1
        lock_j = -1
        for j in range(n,n+n):
            lock_j +=1
            array[i][j] = lock[lock_i][lock_j]

    max_array = len(array)
    
    for r in range(0,4):
        key = rotation(key,m)
        for i in range(0,max_array-m):
            for j in range(0,max_array-m):
            
                # key를 큰 판에 넣고 값을 더함
                for c in range(0,m):
                    for z in range(0,m):
                        array[i+c][j+z] += key[c][z]

                # 지물쇠가 다 1인지 체크
                answer = lock_check(array, m)
                if answer == True:
                    return answer

                # 자물쇠 초기화도 필요
                for c in range(0,m):
                    for z in range(0,m):
                        array[i+c][j+z] -= key[c][z]


    # 회전
    # temp_key = rotation(key,m)
    # print(temp_key)        

    print(array)
    return answer





"""
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]	
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
"""

key = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]	
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

result = solution(key,lock)
print(result)




"""
    # key를 큰 판에 넣음
    for i in range(0,m):
        for j in range(0,m):
            array[i][j] = key[i][j]

"""