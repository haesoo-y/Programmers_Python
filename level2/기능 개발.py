from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    while progresses :
        for i in range(len(speeds)):
            progresses[i] += speeds[i]
        tmp = []
        while progresses:
            if progresses[0] < 100 :
                break
            tmp.append(progresses.popleft())
            speeds.popleft()
        if tmp :
            answer.append(len(tmp))
    return answer