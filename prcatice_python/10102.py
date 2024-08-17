v = int(input())
vote = input()
sum = 0
for i in vote:
    if i == 'A': sum+=1
    else: sum-=1

if sum > 0 : print("A")
elif sum == 0 : print("Tie")
else: print("B")