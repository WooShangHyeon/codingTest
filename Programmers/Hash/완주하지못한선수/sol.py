# import collections
def solution(participant, completion):
    # answer = collections.Counter(participant) - collections.Counter(completion)
    # return list(answer)[0]
    
    hash_dict = {}
    num_sum = 0
    
    for i in participant:
        hash_num = hash(i)
        hash_dict[hash_num]=i
        num_sum += hash_num
    
    for c in completion:
        num_sum -= hash(c)
    
    return hash_dict[num_sum]