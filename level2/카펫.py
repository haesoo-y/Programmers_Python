def solution(brown, yellow):
    answer = []
    for b in range(3, brown):
        a = brown/2 - b + 2
        if (a - 2)*(b - 2) == yellow:
            answer = [a, b]
            break
    return answer