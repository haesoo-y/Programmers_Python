def solution(prices):
    length = len(prices)
    answer = [0] # 답을 뒤부터 담기
    stack = [(prices[-1], length - 1)] # 비교 대상 (값, 인덱스) 스택

    for i in range(length-2,-1,-1):
        while stack and stack[-1][0] >= prices[i]:
            stack.pop()
        if not stack :
            answer.append(length - 1 - i)
        else :
            answer.append(stack[-1][1] - i)
        stack.append((prices[i], i))
    return list(reversed(answer))