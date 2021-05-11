def solution(n, times):
    answer = 0
    start = 0
    end = max(times) * n
    while start <= end :
        mid = (start + end)//2
        total = 0
        for time in times:
            total += mid//time
        if total >= n :
            answer = mid
            end = mid - 1
        else :
            start = mid + 1
    return answer