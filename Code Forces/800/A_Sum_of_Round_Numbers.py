t=int(input())
for _ in range(t):
    n=int(input())
    l=[]
    f=10
    while n>0:
        curr=n%10
        if curr!=0:
            l.append(curr*(f//10))
        f=f*10
        n//=10
    print(len(l))
    print(*l)
