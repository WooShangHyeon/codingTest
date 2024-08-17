n = int(input())
for _ in range(n) :
    ox = input()
    temp = ''
    point = 1
    result = 0
    for i in ox:
        if i == 'O': 
            result += point
        else: point = 1     
        temp = i
        if temp == 'O' : point += 1
    print(result)