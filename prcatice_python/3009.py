a1,a2 = map(int,input().split())
b1,b2 = map(int,input().split())
c1,c2 = map(int,input().split())
res_x, res_y = 0 , 0
if a1==b1: res_x = c1
elif a1==c1: res_x = b1
else: res_x = a1
if a2==b2: res_y = c2
elif a2==c2: res_y = b2
else: res_y = a2
print(res_x,res_y)
    