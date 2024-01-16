def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        cur = commands[i]
        x = []
        for idx in range(cur[0]-1, cur[1]):
            x.append(array[idx])
        x.sort()
        answer.append(x[cur[2]-1])
    return answer

    # return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))


