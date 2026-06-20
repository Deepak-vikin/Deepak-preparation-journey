class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i,v in enumerate(nums):
            if target-v in d:
                return [d[target-v],i]
            d[v]=i

obj=Solution()
res=obj.twoSum([2,7,11,15],9)
print(res)