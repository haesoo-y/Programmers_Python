def is_changable(x, y):
    length = len(x)
    diff = 0
    for i in range(length):
        if x[i] != y[i]:
            diff += 1
    if diff == 1:
        return True
    else:
        return False


def bfs(gph, t):
    lst = list()
    lst.append(0)
    count = 0
    while count < len(gph):
        count += 1
        tmp = []
        for i in lst:
            if t in gph[i]:
                return count
            tmp += gph[i]
        lst = tmp
    return 0


def solution(begin, target, words):
    if target not in words:
        return 0
    graph = [[] for _ in range(len(words) + 1)]
    words = [begin] + words
    for i in range(len(words)):
        for j in range(1, len(words)):
            if is_changable(words[i], words[j]):
                graph[i].append(j)

    answer = bfs(graph, words.index(target))
    return answer