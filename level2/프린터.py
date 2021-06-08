from collections import deque


def solution(priorities, location):
    queue = deque()
    for i in range(len(priorities)):
        v, p = i, priorities[i]
        queue.append((v, p))
    print(queue)
    priorities.sort()
    count = 0
    answer = len(priorities)
    while queue:
        big = priorities[-1]
        tp = queue.popleft()
        if tp[1] == big:
            priorities.pop()
            count += 1
            if tp[0] == location:
                answer = count
                break
        else:
            queue.append(tp)

    return answer