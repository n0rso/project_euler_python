n = 20
lst = []
for i in range(2, n+1):
    for j in range(2, int((i//2)+1)):
        if i % j == 0:

            break
    else:
        lst.append(i)
print (lst)
print(len(lst))
k=1
t=1
for z in range (0,len(lst)):
    while int(lst[z])**k<=n:
        k+=1
        if int(lst[z])**k>n:
            t=t*int(lst[z])**(k-1 )


print(t)


