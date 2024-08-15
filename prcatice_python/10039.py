avr = 0
for _ in range(5):
    n = int(input())
    if n < 40: 
        avr+=40
        continue
    avr+=n
print(int(avr/5))