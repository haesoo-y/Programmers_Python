def solution(n):
    answer = 0
    bool_lst = [True] * (n+1)
    bool_lst[1] = False
    for i in range(2, n + 1):
        if not bool_lst[i]:
            continue
        for k in range(i+i, n+1, i):
            bool_lst[k] = False
    for i in range(1, n+1) :
        if bool_lst[i] :
            answer += 1
    return answer