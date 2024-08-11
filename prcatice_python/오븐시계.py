# a b 각각 현재 시각, 시와 분
# c 요리에 필요한 시간

# 23:59분 이후에는 00:00

a,b = map(int,input().split())
c = int(input())
c_1 = c // 60 #요리시간 시 구하기
c_2 = c % 60 #요리시간 분 구하기

res_h = a+c_1 
res_t = b+c_2

if res_t >=60 : # 분 60 이상일때
    res_h += res_t // 60 # 몫만큼 더해주면 됨
    res_t = res_t % 60 # 분은 나머지가됨

if res_h >= 24: # 24시 넘어갈때
    res_h -= 24
print(f"{res_h} {res_t}")