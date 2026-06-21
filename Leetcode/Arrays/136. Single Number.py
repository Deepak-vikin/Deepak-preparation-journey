class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a=0
        for i in nums:
            a^=i
        return a
obj=Solution()
res=obj.singleNumber([4,1,2,1,2])
print(res)