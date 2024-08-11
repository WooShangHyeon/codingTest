import sys
num = sys.stdin.readline().strip()
num_list = list(map(int,num.split()))
num_list.sort()
print(num_list[1])