# from itertools import permutations
# def solution(numbers):
#     answer = 0
#     all_case = set()
#     for length in range(1,len(numbers)+1):
#         for p in permutations(numbers,length):
#             if p not in all_case:
#                 all_case.add(int("".join(p)))
#     for case in all_case:
#         if isPrime(case):
#             print(case)
#             answer+=1
#     print(all_case)
#     return answer

# def isPrime(num):
#     if num == 0 or num == 1: return False
#     elif num == 2: return True

#     for i in range(2,num//2+1):
#         if num%i == 0:
#             return False
#     return True

##################

# from itertools import permutations
# def solution(n):
#     a = set()
#     for i in range(len(n)):
#         a |= set(map(int, map("".join, permutations(list(n), i + 1))))
#         print(a)
#     a -= set(range(0, 2))
#     print("-------------------")
#     print(a)
#     for i in range(2, int(max(a) ** 0.5) + 1):
#          print(range(i * 2, max(a) + 1, i))
#          a -= set(range(i * 2, max(a) + 1, i))
#     return len(a)

# solution("011")

print(set(range(1,6)))
# for i in range(2, 6):
#     multiples_set = set(range(i * 2, 15 + 1, i))
#     print(f"For i = {i}, multiples_set = {multiples_set}")
