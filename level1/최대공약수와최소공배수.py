from math import gcd
def solution(n, m):
    gcd_num = gcd(n, m)
    lcm_num = n*m // gcd(n,m)
    answer = [gcd_num, lcm_num]
    return answer