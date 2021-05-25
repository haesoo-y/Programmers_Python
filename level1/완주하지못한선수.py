def solution(participant, completion):
    answer = ''
    dic = dict()
    for p in participant:
        dic[p] = dic.get(p, 0) + 1
    for c in completion:
        dic[c] -= 1
        if dic[c] == 0:
            del dic[c]
    for key in dic.keys():
        answer += key

    return answer