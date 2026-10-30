"""
You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

Return the maximum absolute sum of any (possibly empty) subarray of nums.

Note that abs(x) is defined as follows:

If x is a negative integer, then abs(x) = -x.
If x is a non-negative integer, then abs(x) = x.


Example 1:

Input: nums = [1,-3,2,3,-4]
Output: 5
Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.
"""
class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        max_ans=0
        curr=0
        for i in range(len(nums)):
            curr+=nums[i]
            max_ans=max(max_ans,curr)
            if curr<0:
                curr=0
        min_ans=0
        curr=0
        for i in range(len(nums)):
            curr+=nums[i]
            min_ans=min(min_ans,curr)
            if curr>0:
                curr=0
        return max(max_ans,abs(min_ans))
obj=Solution()
res=obj.maxAbsoluteSum(nums = [1,-3,2,3,-4])
print(res)
