import math
def solution(w,h):
    gcd_num = math.gcd(w,h)
    answer = (w * h) - (w + h - gcd_num)
    return answer