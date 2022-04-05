# 크레인 인형 뽑기 게임


def solution(board, moves):
    basket = []
    answer = 0
    for i in range(0,len(moves)):
        temp = moves[i] - 1
        for j in range(0,len(board)):
            if board[j][temp] == 0:
                continue
            else:
                basket.append(board[j][temp])
                board[j][temp] = 0
                break

        if len(basket) >= 2:
            if basket[-1] == basket[-2]:
                basket.pop()
                basket.pop()
                answer += 2
        
    return answer




board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

result = solution(board, moves)

print(result)