t=int(input())
for _ in range(t):
    k=int(input())
    nums=list(map(int,input().split()))
    count=0
    for num in nums:
        if num>=2:
            count+=1
    if any(num>2 for num in nums) or count>=2:
        print("YES")
    else:
        print("NO")
