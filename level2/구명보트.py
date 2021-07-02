def solution(people, limit):
    answer = 0 # 카운트이자 인덱스
    people.sort(reverse=True) # 내림차순 정렬
    while answer < len(people):
        this = people[answer]
        while this + people[-1] <= limit :
            this += people.pop()
        answer += 1
    return answer