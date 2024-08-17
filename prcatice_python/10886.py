n = int(input())
vote_sum = 0
for _ in range(n):
    vote = int(input())
    if vote > 0 : vote_sum += 1
    else : vote_sum -= 1
if vote_sum > 0 : print("Junhee is cute!")
else: print("Junhee is not cute!")