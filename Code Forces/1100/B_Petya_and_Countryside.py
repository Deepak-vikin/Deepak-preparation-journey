ans=0
n=int(input())
nums=list(map(int,input().split()))
curr_max=0
for i in range(n):
    num=nums[i]
    if num>=curr_max:
        j=i
        curr=nums[i]
        count=0
        while j>=0 and nums[j]<=curr:
            if i==j:
                j-=1
                continue
            curr=nums[j]
            count+=1
            j-=1
        j=i
        curr=nums[i]
        while j<n and nums[j]<=curr:
            curr=nums[j]
            count+=1
            j+=1
        ans=max(ans,count)
print(ans)
