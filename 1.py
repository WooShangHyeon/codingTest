# def solution(priorities, location):
#     queue =  [(i,p) for i,p in enumerate(priorities)]
#     for i in queue:
#         print(i[0])
#         print(i[1])
#     # answer = 0
#     # while True:
#     #     cur = queue.pop(0)
#     #     if any(cur[1] < q[1] for q in queue):
#     #         queue.append(cur)
#     #     else:
#     #         answer += 1
#     #         if cur[0] == location:
#     #             return answer
from collections import deque
def solution(priorities, location):
    index_list = deque([i for i in range(len(priorities))])
    maximum = max(priorities)
    print(index_list)
solution([2, 1, 3, 2],2)