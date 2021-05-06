import heapq

INF = int(1e9)


def dijkstra(x, y):
    num = len(graph)
    distance = [INF] * (num + 1)
    distance[x] = 0
    pq = [[0, x]]  # (비용, 지점) 을 담은 우선순위 큐
    while pq:
        c, z = heapq.heappop(pq)
        if distance[z] < c:
            continue
        for i in graph[z]:
            ncost = c + i[1]  # z를 거쳐서 i[0] 에 가는 비용
            if ncost < distance[i[0]]:  # i[0] 에 가는 비용보다 작으면
                distance[i[0]] = ncost
                heapq.heappush(pq, (ncost, i[0]))
    return distance[y]  # x에서 y로 가는 최소 비용


def solution(n, s, a, b, fares):
    answer = INF
    global graph
    graph = [[] for i in range(n + 1)]  # 각 인덱스에 (지점z, 비용c) 저장할 것
    for fare in fares:
        graph[fare[0]].append((fare[1], fare[2]))
        graph[fare[1]].append((fare[0], fare[2]))

    for i in range(1, n + 1):
        answer = min(answer, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))
        print('answer', answer)

    return answer