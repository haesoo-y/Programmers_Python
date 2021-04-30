def solution(s):
    answer = []
    s = list(s[2:-2].split('},{'))
    s.sort(key=len)
    for i in s:
        tmp = i.split(',')
        for j in tmp:
            if int(j) in answer:
                continue
            else:
                answer.append(int(j))

    return answer