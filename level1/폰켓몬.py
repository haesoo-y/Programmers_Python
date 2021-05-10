def solution(nums):
    mon_lst = list(set(nums))
    if len(mon_lst) >= len(nums)//2 :
        answer = len(nums)//2
    else :
        answer = len(mon_lst)
    return answer