t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    m=len(a)
    s=0
    while len(a)>=k:
        m=len(a)
        if k<=m and a[k-1]>a[m-k]:
            s+=a[k-1]
            a.pop(k-1)
        elif m-k < m:
            s+=a[m-k]
            a.pop(m-k)
        else:
            break
    print(s)        