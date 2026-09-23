n,m=map(int,input().split())
count=0
while n<=m:
    n*=3
    m*=2
    count+=1
print(count)

