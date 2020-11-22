lst=[2]
for i in range(3,2000000):
    for j in lst:
        if i%j==0:
            break
    else:
        lst.append(i)

sum=sum(lst)
print(sum)
