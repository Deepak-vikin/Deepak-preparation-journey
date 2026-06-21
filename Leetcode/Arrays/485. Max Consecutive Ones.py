class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i=0
        c=0
        m=0
        while i<len(nums):
            if nums[i]!=1:
                c=max(c,m)
                m=0
            else:
                m+=1
            i+=1
        c=max(c,m)
        return c
obj=Solution()
res=obj.findMaxConsecutiveOnes([1,0,1,0,1,0,1])
print(res)