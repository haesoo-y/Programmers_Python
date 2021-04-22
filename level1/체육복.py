def solution(n, lost, reserve):
    answer = n - len(lost)
    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i] == reserve[j]:
                lost[i] = -1
                reserve[j] = -1
    for i in range(len(reserve)):
        if reserve[i] == -1:
            continue
        for j in range(len(lost)):
            if reserve[i] + 1 == lost[j] or reserve[i] - 1 == lost[j]:
                lost[j] = -1
                break
    answer += lost.count(-1)

    return answer