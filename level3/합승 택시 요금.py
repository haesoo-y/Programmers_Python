INF = int(1e9)
def solution(n, s, a, b, fares):
    answer = INF
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    # 비용 정리
    for i in range(1, n + 1):
        graph[i][i] = 0
    for fare in fares:
        graph[fare[0]][fare[1]] = fare[2]
        graph[fare[1]][fare[0]] = fare[2]

    # 플로이드 워셜
    for k in range(1, n + 1):
        for x in range(1, n + 1):
            for y in range(1, n + 1):
                graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])

    # 답 구하기 a,b 가 흩어지는 지점: k
    for k in range(1, n + 1):
        answer = min(answer, graph[s][k] + graph[k][a] + graph[k][b])

    return answer