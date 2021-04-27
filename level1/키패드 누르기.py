def solution(numbers, hand):
    answer = ''
    left = [1, 4, 7, '*']
    center = [2, 5, 8, 0]
    right = [3, 6, 9, '#']
    position = {'left':'*', 'right':'#'}
    finger = {'right': 'R', 'left': 'L'}
    for i in numbers:
        # 왼쪽 위치 번호일 때
        if i in left:
            position['left'] = i
            answer += 'L'
        # 오른쪽 위치 번호일 때
        elif i in right:
            position['right'] = i
            answer += 'R'
        # 가운데 위치 번호일 때
        else :
            index = center.index(i)
            # 양 손가락이 모두 가운데
            if position['left'] in center and position['right'] in center:
                if abs(index-center.index(position['left'])) < abs(index-center.index(position['right'])):
                    answer += 'L'
                    position['left'] = i
                elif abs(index-center.index(position['left'])) > abs(index-center.index(position['right'])):
                    answer += 'R'
                    position['right'] = i
                else :
                    answer += finger[hand]
                    position[hand] = i
            # 왼 손가락만 가운데
            elif position['left'] in center :
                if abs(index-center.index(position['left'])) < abs(index-right.index(position['right']))+1:
                    answer += 'L'
                    position['left'] = i
                elif abs(index-center.index(position['left'])) > abs(index-right.index(position['right']))+1:
                    answer += 'R'
                    position['right'] = i
                else :
                    answer += finger[hand]
                    position[hand] = i
            # 오른 손가락만 가운데
            elif position['right'] in center :
                if abs(index-left.index(position['left']))+1 < abs(index-center.index(position['right'])):
                    answer += 'L'
                    position['left'] = i
                elif abs(index-left.index(position['left']))+1 > abs(index-center.index(position['right'])):
                    answer += 'R'
                    position['right'] = i
                else :
                    answer += finger[hand]
                    position[hand] = i
            # 양 손가락이 가운데가 아닐 때
            else :
                if abs(index-left.index(position['left'])) < abs(index-right.index(position['right'])):
                    answer += 'L'
                    position['left'] = i
                elif abs(index-left.index(position['left'])) > abs(index-right.index(position['right'])):
                    answer += 'R'
                    position['right'] = i
                else :
                    answer += finger[hand]
                    position[hand] = i
    return answer