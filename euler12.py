import math

def trian(n):
    s = 0
    while n > 0:
        s += n
        n -= 1

    return s

def div(n):
    s = 0
    for i in range(1, n + 1):
        if n % i == 0:
            s += 1
    return s

i=28
while div(trian(i))<500:
    i+=1

print(i)