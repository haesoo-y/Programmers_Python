def solution(stones, k):
    left, right = 0, max(stones)
    while left <= right:
        mid = (left + right) // 2
        zero = 0
        for stone in stones:
            if stone - mid <= 0:
                zero += 1
                if zero == k:  # 못건너는 값이 나타나면
                    answer = mid
                    right = mid - 1
                    break
            else:
                zero = 0
        if zero < k:  # 찾지 못했다면
            left = mid + 1

    return answer