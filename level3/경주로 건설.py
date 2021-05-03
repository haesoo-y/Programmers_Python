from collections import deque

def bfs(graph):
    n = len(graph)
    queue = deque() # x, y, head, cost
    visited = dict() # (x, y, head) : cost
    result = int(1e9)
    if graph[0][1] == 0:
        visited[(0,0,1)] = 0
        queue.append((0, 0, 1, 0))
    if graph[1][0] == 0:
        visited[(0,0,2)] = 0
        queue.append((0,0,2,0))
    dx = [-1, 0, 1, 0] # 0  1  2  3
    dy = [0, 1, 0, -1] # 위 오 아래 왼
    while queue:
        x, y, head, cost = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 새로운 방향은 i
            if nx < 0 or ny < 0 or nx >= n or ny >= n or graph[nx][ny] == 1:
                continue
            if abs(head - i) % 2 == 0 : # 방향일치 그냥 직진
                ncost = cost + 100
            else : # 코너 돌고 직진
                ncost = cost + 600
            # 목적지에 도달했는지 안했는지 체크
            if nx == n - 1 and ny == n - 1:
                result = min(result, ncost) # 비교해서 작은 비용 계속 넣어줌
            # 방문하지 않았거나 비용이 더 작아진 경우 갱신
            elif not visited.get((nx, ny, i)) or visited.get((nx, ny, i)) > ncost:
                visited[(nx, ny, i)] = ncost
                queue.append((nx, ny, i, ncost))
    return result

def solution(board):
    answer = bfs(board)
    return answer