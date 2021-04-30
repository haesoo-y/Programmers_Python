import sys

sys.setrecursionlimit(1000000)


def find_room(n):
    if n not in next_room:
        next_room[n] = n + 1
        return n

    next = find_room(next_room[n])
    next_room[n] = next + 1
    return next


def solution(k, room_number):
    global next_room
    next_room = dict()
    answer = []
    for i in room_number:
        num = find_room(i)
        answer.append(num)

    return answer