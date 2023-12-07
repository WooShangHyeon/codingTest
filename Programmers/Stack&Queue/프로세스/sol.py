
# 첫번째 풀이
def solution(priorities, location):
    answer = 0
    #인덱스
    cur_idx = -1
    max_idx = -1
    #Max priority
    max_prio = 0
    
    while True:
        # 현재 인덱스가 마지막 인덱스일때와 아닐때
        if(cur_idx == len(priorities)-1) : cur_idx = 0
        else: cur_idx += 1 
        
        #현재 인덱스가 Max 인덱스와 같을때 (이 경우 Max idx 확정)
        if(cur_idx == max_idx):
            answer += 1
            priorities[max_idx] = 0
            # 특정 프로세스의 우선순위가 0이면 종료
            if(priorities[location] == 0): break  
            # Max 인덱스가 마지막 인덱스 일때
            if(max_idx == len(priorities)-1):
                cur_idx = 0
            max_prio = 0
            
        # Max prio 찾기
        if(priorities[cur_idx] > max_prio):
            max_prio = priorities[cur_idx]
            max_idx = cur_idx
        
    return answer


# 아래는 추가적인 다른 풀이
def solution1(priorities, location):
		# 인덱스,prio 튜플로 리스트에 저장
    queue =  [(idx,prio) for idx,prio in enumerate(priorities)]
    answer = 0
    while True:
				# Max 찾기
        cur = queue.pop(0)
				# [0]은 index, [1]은 prio
        if any(cur[1] < q[1] for q in queue):
				# queue안에 큰게 있을경우 실행
            queue.append(cur)
        else:
            answer += 1
						# location인덱스 값이 max이면
            if cur[0] == location:
                return answer
            

def solution2(priorities, location):
    answer = 0
    max_prio = max(priorities)
    while True:
        cur_prio = priorities.pop(0)
        if max_prio == cur_prio:
            answer += 1
            if location == 0:
                break
            else:
                location -= 1
            max_prio = max(priorities)
        else:
            priorities.append(cur_prio)
            if location == 0:
                location = len(priorities)-1
            else:
                location -= 1
    return answer