def solution(numbers, hand):
    answer = ''
    left_lst = [1, 4, 7, '*']
    right_lst = [3, 6, 9, '#']
    mid_lst = [2, 5, 8, 0]
    left = '*'
    right = '#'
    for i in numbers:
        if i in left_lst:
            left = i
            answer += 'L'
        elif i in right_lst:
            right = i
            answer += 'R'
        else:  # 이번 번호가 중간 번호일 경우
            left_diff = abs(left_lst.index(left) - mid_lst.index(i)) + 1 if left in left_lst else abs(
                mid_lst.index(left) - mid_lst.index(i))
            right_diff = abs(right_lst.index(right) - mid_lst.index(i)) + 1 if right in right_lst else abs(
                mid_lst.index(right) - mid_lst.index(i))
            if left_diff < right_diff:
                left = i
                answer += 'L'
            elif left_diff > right_diff:
                right = i
                answer += 'R'
            else:
                if hand == 'left':
                    answer += 'L'
                    left = i
                else:
                    answer += 'R'
                    right = i

    return answer