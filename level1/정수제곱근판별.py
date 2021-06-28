def solution(n):
    sqrt = int(n**(1/2))
    return (sqrt+1)**2 if sqrt**2 == n else -1