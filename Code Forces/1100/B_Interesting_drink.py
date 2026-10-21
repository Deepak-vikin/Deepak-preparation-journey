n=int(input())
nums=list(map(int,input().split()))
nums.sort()
q=int(input())
for _ in range(q):
    num=int(input())
    left=0
    right=len(nums)-1
    while left<=right:
        mid=(left+right)//2
        if num<nums[mid]:
            right=mid-1
        else:
            left=mid+1
    print(left)