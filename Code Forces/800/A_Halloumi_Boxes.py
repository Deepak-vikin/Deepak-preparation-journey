t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    boxes=list(map(int,input().split()))
    if boxes==sorted(boxes):
        print("YES")
    else:
        if k==1:
            print("NO")
        else:
            print("YES")