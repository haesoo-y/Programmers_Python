from itertools import combinations
from bisect import bisect_left

def make_dic(lst):  # 모든 경우의 수를 담은 딕셔너리 만들기
    dic = dict()
    for string in lst:
        tmp_lst = string.split()  # ['java', 'backend', 'junior', 'pizza', '150']
        for i in range(5):  # 0개 고를 때 ~ 4개 고를 때
            for tpl in list(combinations([0, 1, 2, 3], i)):  # 0~3 중에 i개 고르는 튜플 tpl
                tmp = ''
                for j in range(4):
                    if j in tpl:
                        tmp += tmp_lst[j]
                    else:
                        tmp += '-'
                if dic.get(tmp):
                    dic[tmp].append(int(tmp_lst[4]))
                else:
                    dic[tmp] = [int(tmp_lst[4])]

    for key in dic.keys():
        dic[key].sort()

    return dic

def solution(info, query):
    answer = []
    all_info = make_dic(info)
    for q in query:
        q_lst = q.split()
        target = q_lst[0] + q_lst[2] + q_lst[4] + q_lst[6]
        if target not in all_info.keys():
            answer.append(0)
            continue
        index = bisect_left(all_info[target], int(q_lst[7]))
        answer.append(len(all_info[target]) - index)

    return answer