"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.



Example 1:

Input: nums = [3,0,1]

Output: 2

Explanation:

n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x=0
        for i in range(len(nums)+1):
            x^=i
        y=0
        for i in range(len(nums)):
            y^=nums[i]
        print(x,y)
        return x^y
obj=Solution()
res=obj.missingNumber([3,0,1])
print(res)

