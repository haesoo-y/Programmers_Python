def solution(new_id):
    answer = ''
    # 1 단계
    new_id = new_id.lower()
    print('1단계 완료', new_id)
    # 2 단계
    for c in new_id:
        if c.isalnum() or c == '-' or c == '_' or c == '.':
            answer += c
    new_id = answer
    print('2단계 완료', new_id)
    # 3 단계
    while new_id.find('..') != -1:
        new_id = new_id.replace('..', '.')
    print('3단계 완료', new_id)
    # 4 단계
    if new_id and new_id[0] == '.':
        new_id = new_id[1:]
    if new_id and new_id[-1] == '.':
        new_id = new_id[:len(new_id) - 1]
    print('4단계 완료', new_id)
    # 5 단계
    if not new_id:
        new_id = 'a'
    print('5단계 완료', new_id)
    # 6 단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:14]
    print('6단계 완료', new_id)
    # 7 단계
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]
    print('7단계 완료', new_id)
    answer = new_id

    return answer