def solution(prices):
    answer = []
    prices.reverse()
    # 1. 모든 인덱스에 대하여 각각 인덱스를 기준으로 떨어질때까지 초를 센다.
    # 2. 떨어지면 그때까지의 초를 answer에 append하고 다음 인덱스로 넘어간다.
    
    while prices:
        pivot = prices.pop()
        sec = 0
        for i in range(len(prices)-1,-1,-1):
            sec += 1
            if prices[i] < pivot: break
        answer.append(sec)
    return answer


'''
1. from collections import deque 이용

from collections import deque

def solution(prices):
    queue = deque(prices)
    answer = []
    
    while queue:
        price = queue.popleft()
        sec = 0
        for q in queue:
            sec += 1
            if price > q:
                break 
        answer.append(sec)        
    return answer


2. stack을 이용

def solution(prices):
    length = len(prices)
    answer = [ i for i in range (length - 1, -1, -1)]
    
    stack = [0]
    for i in range (1, length, 1):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer
'''