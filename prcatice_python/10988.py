a = input()
check = 1
for i in range(0,len(a)//2+1):
    if a[i] != a[len(a)-1-i] : 
        print(0)
        check = 0
        break
if check : print(1)


'''
alp =list(str(input()))

if list(reversed(alp)) == alp:
    print(1)
else:
    print(0)
'''