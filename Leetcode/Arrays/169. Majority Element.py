class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
obj=Solution()
res=obj.majorityElement([3,2,3])
print(res)