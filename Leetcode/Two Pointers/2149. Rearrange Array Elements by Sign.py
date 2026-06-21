class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res=[]
        i=0
        j=0
        while i<len(nums) and j<len(nums):
            while nums[i]<0:
                i+=1
            while nums[j]>0:
                j+=1
            res.append(nums[i])
            res.append(nums[j])
            i+=1
            j+=1
        return res
obj=Solution()
res=obj.rearrangeArray([3,1,-2,-5,2,-4])
print(res)