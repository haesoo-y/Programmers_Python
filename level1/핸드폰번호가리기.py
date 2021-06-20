def solution(phone_number):
    answer = ''
    phone_length = len(phone_number)
    for i in range(phone_length):
        if i >= (phone_length - 4):
            c = phone_number[i]
        else :
            c = '*'
        answer += c
    return answer