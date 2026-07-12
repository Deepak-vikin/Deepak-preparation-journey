"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.



Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        ans = 0
        f = {}
        for right in range(len(nums)):
            if nums[right] in f:
                f[nums[right]] += 1
            else:
                f[nums[right]] = 1
            while 0 in f:
                if nums[left] in f:
                    if f[nums[left]] > 1:
                        f[nums[left]] -= 1
                    else:
                        del f[nums[left]]
                left += 1
            ans = max(ans, right - left + 1)
        return ans

obj=Solution()
res=obj.findMaxConsecutiveOnes([1,1,0,1,1,1])
print(res)