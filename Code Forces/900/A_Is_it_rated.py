n=int(input())
prev=float("inf")
lst=[]
for _ in range(n):
    start,end=map(int,input().split())
    if start!=end:
        print("rated")
        break
    lst.append((start,end))
else:
    for i in range(1,len(lst)):
        if lst[i][0]>lst[i-1][0]:
            print("unrated")
            break
    else:
        print("maybe")
