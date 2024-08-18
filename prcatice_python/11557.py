t = int(input())
for _ in range(t):
    n = int(input())
    max_L = 0
    max_S = ''
    for _ in range(n):
        S , L = map(str, input().split())
        if max_L < int(L): 
            max_S = S
            max_L = int(L)
    print(max_S)