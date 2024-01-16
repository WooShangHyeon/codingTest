# def solution(citations):
#     citations.sort(reverse=True)
#     for idx , citation in enumerate(citations):
#         if idx >= citation:
#             return idx
#     return len(citations)
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer