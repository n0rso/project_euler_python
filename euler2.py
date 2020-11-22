def fibo(x):
    if x == 1:
        return 0
    elif x == 2:
        return 1
    else:
        return fibo(x - 1) + fibo(x - 2)


i = 1
sum = 0
while fibo(i) <= 4000000:
  i+=1
  if int(fibo(i)) % 2 == 0:
        sum = sum + int(fibo(i))


print(sum)
