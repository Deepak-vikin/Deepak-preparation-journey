a,b=map(int,input().split())
nums1=list(map(int,input().split()))
nums2=list(map(int,input().split()))
nums1.sort()
def binary_search(target):
    left=0
    right=len(nums1)-1
    while left<=right:
        mid=(left+right)//2
        if target<nums1[mid]:
            right=mid-1
        else:
            left=mid+1
    return left
for num in nums2:
    print(binary_search(num),end=" ")
