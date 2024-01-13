def solution(nums):
    pocket_dict = { x : True for x in nums}
    answer = len(pocket_dict)
    if answer >= len(nums)/2 : return len(nums)/2
    return answer