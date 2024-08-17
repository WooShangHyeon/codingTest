str_list = input()
temp=''
result=0
for i in str_list:
    if i ==temp:result+=5
    else: result+=10
    temp = i
print(result)