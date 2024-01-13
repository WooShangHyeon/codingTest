def solution(clothes):
    # from collections import Counter
    # from functools import reduce
    # cnt = Counter([kind for name, kind in clothes])
    # answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    # return answer

    answer = 1
    clothes_hash = {}
    
    for cloth in clothes:
        hash_key = cloth[1]
        hash_value = cloth[0]
        
        if hash_key in clothes_hash:
            clothes_hash[hash_key] += 1
        else:
            clothes_hash[hash_key] = 1
    
    for x in clothes_hash:
        answer *= clothes_hash[x]+1
        
    return answer-1