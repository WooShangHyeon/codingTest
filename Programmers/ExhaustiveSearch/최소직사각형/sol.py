def solution(sizes):
    max_len = []
    min_len = []
    for size in sizes:
        max_len.append(max(size))
        min_len.append(min(size))
    
    return max(max_len)*max(min_len)