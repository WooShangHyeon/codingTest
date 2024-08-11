num = int(input())
check=True
while check:
    if num==1: check=False
    else:
        for i in range(2,num+1):
            if num%i == 0:
                print(i)
                if i==num:

                    check=False
                    break
                num = num//i
                break