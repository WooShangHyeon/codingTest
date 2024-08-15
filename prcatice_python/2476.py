num = int(input())
max_money = 0
for i in range(num):
    a,b,c=map(int, input().split())
    money = 0
    if a==b and a==c: money = 10000+a*1000
    elif a==b or b==c: money = 1000+b*100
    elif a==c: money = 1000+a*100
    else: money = max(a,b,c)*100
    if money >= max_money: max_money = money
print(max_money)