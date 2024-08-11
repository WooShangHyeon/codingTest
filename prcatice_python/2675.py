num = int(input())
for i in range(num):
    str = input().split()
    res =''
    for i in str[1]:
        res += i*int(str[0])
    print(res)