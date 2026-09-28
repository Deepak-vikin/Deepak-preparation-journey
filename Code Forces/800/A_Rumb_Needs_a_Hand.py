t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    target=[]
    for i in range(1,n+1):
        target.append(i)
    curr=[]
    idx=[]
    for i in range(n):
        if arr[i]!=i+1:
            curr.append(arr[i])
            idx.append(i)
    curr=curr[::-1]
    for i in range(len(idx)):
        arr[idx[i]]=curr[i]
    print('YES' if arr==target else "NO")
