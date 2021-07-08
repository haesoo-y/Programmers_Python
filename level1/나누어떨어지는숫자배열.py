def solution(arr, divisor):
    return sorted([num for num in arr if num % divisor == 0]) or [-1]