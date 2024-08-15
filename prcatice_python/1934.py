T = int(input())
for _ in range(T):
    a,b = map(int,input().split())
    a_temp, b_temp = a,b
    while a%b != 0:
        a,b = b,a%b
    print(int(a_temp*b_temp/b))
   