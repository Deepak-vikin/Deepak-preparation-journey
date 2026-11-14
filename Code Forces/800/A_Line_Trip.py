t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    gas=list(map(int,input().split()))
    ans=gas[0]
    for i in range(1,n):
        ans=max(ans,gas[i]-gas[i-1])
    ans=max(ans,(x-gas[-1])*2)
    print(ans)