from itertools import combinations
from bisect import bisect_left


def make_cases(lst):
    results = []
    for k in range(5):  # k개를 뽑을 경우
        for t in combinations([0, 1, 2, 3], k):
            result = ''
            for i in range(4):
                if i in t:
                    result += lst[i]
                else:
                    result += '-'
            results.append(result)
    return results


def solution(info, query):
    answer = []
    all_people = {}
    for i in info:
        info_lst = [x for x in i.split()]
        cases = make_cases(info_lst)
        for case in cases:
            if all_people.get(case):
                all_people[case].append(int(info_lst[-1]))
            else:
                all_people[case] = [int(info_lst[-1])]

    for key in all_people.keys():
        all_people[key].sort()

    for q in query:
        query_lst = [x for x in q.split()]
        target = query_lst[0] + query_lst[2] + query_lst[4] + query_lst[6]
        if target in all_people.keys():
            length = len(all_people[target])
            index = bisect_left(all_people[target], int(query_lst[-1]))
            answer.append(length - index)
        else:
            answer.append(0)

    return answer