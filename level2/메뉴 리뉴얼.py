from itertools import combinations


def solution(orders, course):
    answer = []
    for i in course:
        dic = dict()
        for string in orders:
            if len(string) < i:
                continue
            # tmps i개씩 뽑은 조합 리스트
            tmps = list(combinations(string, i))
            for tmp in tmps:
                tmp = list(tmp)
                tmp.sort()
                tmp = ''.join(tmp)
                dic[tmp] = dic.get(tmp, 0) + 1
            # 각 문자열이 나온 횟수를 딕셔너리에 저장
        if not dic:
            continue
        # sort_lst에 횟수기준으로 딕셔너리 정렬
        sort_lst = sorted(dic.items(), key=lambda x: -x[1])
        max_num = sort_lst[0][1]
        print(max_num, "maxnum")
        # 최대 횟수와 일치하는 문자열 모두 answer에 담음
        print("sort_lst", sort_lst)
        for k in range(len(sort_lst)):
            if sort_lst[k][1] == max_num and sort_lst[k][1] >= 2:
                answer.append(sort_lst[k][0])
            else:
                break

    print("answer", answer)
    answer.sort()
    return answer