S = int(input())
num = 0
result = 0
for i in range(1,S+1):
    num += i
    result = i
    if num > S:
        result -= 1
        break
print(result)