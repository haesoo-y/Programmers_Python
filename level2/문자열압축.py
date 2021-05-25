def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2 + 1):
        lst = []
        tmp = ''
        count = 0
        for j in range(len(s)):
            count += 1
            tmp += s[j]
            if count == i:
                lst.append(tmp)
                count = 0
                tmp = ''
            if j == len(s) - 1:
                lst.append(tmp)
        lst.append('')
        tmp = ''
        count = 1
        base = lst[0]
        # print(lst)
        for j in range(1, len(lst)):
            if lst[j] == base :
                count += 1
            else :
                if count == 1:
                    tmp += base
                else :
                    tmp += str(count) + base
                count = 1
                base = lst[j]
        # print(tmp)
        answer = min(answer, len(tmp))
    # print(answer)
    return answer