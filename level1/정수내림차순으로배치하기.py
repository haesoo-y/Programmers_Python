def solution(n):
    answer = sorted([c for c in str(n)], reverse=True)
    return int(''.join(answer))