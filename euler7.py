prime = [2]
n = 2
while len(prime) < 1001:
    n += 1
    for i in range(2, n + 1):
        for j in prime:
            if i % j == 0:
                break
        else:
            prime.append(i)
print(prime[-1])

