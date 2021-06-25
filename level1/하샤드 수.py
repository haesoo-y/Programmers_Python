def solution(x):
    tmp = 0
    for c in str(x) :
        tmp += int(c)
    return x % tmp == 0