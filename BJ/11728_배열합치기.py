n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

num_sum = []

al, ar = 0, len(A)
bl, br = 0, len(B)

while n+m > 0:
    if n == 0:
        num_sum.append(B[bl])
        if bl < br:
            bl += 1
        m -= 1
    elif m == 0:
        num_sum.append(A[al])
        if al < ar:
            al += 1
        n -= 1
    else:
        if A[al] < B[bl]:
            num_sum.append(A[al])
            if al < ar:
                al += 1
            n -= 1
        else:
            num_sum.append(B[bl])
            if bl < br:
                bl += 1
            m -= 1
print(*num_sum)
