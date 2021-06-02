def solution(numbers):
    answer = ''
    for i in range(len(numbers)):
        numbers[i] = ((str(numbers[i])*4) ,str(numbers[i]))
    numbers.sort(key = lambda x:x[0], reverse=True)
    for n in numbers:
        answer += n[1]
    answer = str(int(answer))
    return answer