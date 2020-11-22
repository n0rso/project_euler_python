import math

n = 13
k = n
i = 2
while i * i < n:
    while n % i == 0:
        n = n / i
    i = i + 1

if k == n:
    if math.sqrt(n)==round(math.sqrt(n)):
        print(math.sqrt(n))
    else:
        print(n)
else:
    print(n)
