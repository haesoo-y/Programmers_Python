from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append(0)
    for i in range(len(numbers)):
        for _ in range(len(queue)):
            x = queue.popleft()
            queue.append(x + numbers[i])
            queue.append(x - numbers[i])
    answer = queue.count(target)
    return answer