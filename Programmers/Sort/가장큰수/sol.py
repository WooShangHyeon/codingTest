
def solution(numbers):
    answer = ''
    arr = list(map(str,numbers))
    arr.sort(key= lambda x: x*3,reverse=True)
    for i in arr:
        answer += i
    

    return str(int(answer))