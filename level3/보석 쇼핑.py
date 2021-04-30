def solution(gems):
    gem_num = len(set(gems))
    max_num = len(gems)
    basket = {gems[0]: 1}
    answer = [1, max_num]
    start, end = 0, 0
    while start < max_num and end < max_num:
        if len(basket) == gem_num:
            if answer[1] - answer[0] > end - start:
                answer = [start + 1, end + 1]
            basket[gems[start]] -= 1
            if basket[gems[start]] == 0:
                del basket[gems[start]]
            start += 1
        else:
            end += 1
            if end == max_num:
                break
            basket[gems[end]] = basket.get(gems[end], 0) + 1

    return answer