from itertools import permutations
def is_match(a, b):
    for i in range(len(a)):
        if is_same(a[i], b[i]):
            continue
        else :
            return False
    return True
def is_same(a, b):
    if len(a) != len(b):
        return False
    length = len(a)
    for i in range(length):
        if b[i] == '*':
            continue
        elif a[i] == b[i]:
            continue
        else :
            return False
    return True

def solution(user_id, banned_id):
    answer = []
    ban_num = len(banned_id)
    lst = list(permutations(user_id, ban_num))
    # 가능한 튜플 가져와서 매칭
    for c in lst:
        if is_match(c, banned_id):
            tmp = set(c)
            if tmp not in answer:
                answer.append(tmp)

    print(answer)
    return len(answer)