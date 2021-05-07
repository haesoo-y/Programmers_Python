def solution(board, moves):
    answer = 0
    stack = [0]
    for i in moves:
        i_ = i - 1
        for lst in board:  # 뽑아서 스택에 추가
            if lst[i_] == 0:
                continue
            else:
                stack.append(lst[i_])
                lst[i_] = 0
                if stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
                    answer += 2
                break

    return answer