class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i]==nums[i-1] and i!=0:
                continue
            j=i+1
            k=len(nums)-1
            while j<k:
                s=nums[i]+nums[j]+nums[k]
                if s<0:
                    j+=1
                    while nums[j]==nums[j-1] and j<k:
                        j+=1
                elif s>0:
                    k-=1
                    while nums[k]==nums[k+1] and j<k:
                        k-=1
                else:
                    v=[nums[i],nums[j],nums[k]]
                    res.append(v)
                    j+=1
                    k-=1
                    while nums[j]==nums[j-1] and j<k:
                        j+=1
                    while nums[k]==nums[k+1] and j<k:
                        k-=1
        return res
obj=Solution()
res=obj.threeSum([-1,0,1,2,-1,-4])
print(res)