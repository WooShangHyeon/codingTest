# @은 3을 곱함, %는 5를 더함, #은 7을뺌
num = int(input())
for i in range(num):
    case = input().split()
    sum = float(case[0])
    for i in range(1,len(case)):
        if case[i] == '@': 
            sum = sum*3
        elif case[i] == '%':
            sum+=5
        elif case[i] == '#':
            sum-=7
    print(f"{sum:.2f}")  