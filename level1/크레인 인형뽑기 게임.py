def solution(board, moves):
    answer = 0
    line = len(board)
    graph = [[] for _ in range(line + 1)]
    basket = []
    # 그래프 만들기
    for i in range(line - 1, -1, -1):
        for j in range(line):
            if board[i][j] == 0:
                continue
            graph[j + 1].append(board[i][j])

    # 뽑아서 바구니에 넣기
    for i in moves:
        if not graph[i]:
            continue
        x = graph[i].pop()
        if basket and basket[-1] == x:
            basket.pop()
            answer += 2
        else:
            basket.append(x)

    return answer