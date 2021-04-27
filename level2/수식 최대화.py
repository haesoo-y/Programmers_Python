def solution(expression):
    answer = []
    calc_lst = [['+', '-', '*'], ['+', '*', '-'], ['*', '+', '-'], ['*', '-', '+'], ['-', '*', '+'], ['-', '+', '*']]
    for a, b, c in calc_lst:
        tmp_lst = []
        for e in expression.split(a):
            tmp = [f'({i})' for i in e.split(b)]
            tmp_lst.append(f'({b.join(tmp)})')
        answer.append(abs(eval(a.join(tmp_lst))))

    return max(answer)