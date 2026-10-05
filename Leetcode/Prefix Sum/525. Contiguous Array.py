"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.



Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
"""
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        left=0
        hash={0:-1}
        ans=0
        curr=0
        for ch in range(len(nums)):
            if nums[ch]==0:
                curr-=1
            else:
                curr+=1
            curr_ans=0
            if curr in hash:
                curr_ans=ch-hash[curr]
            else:
                hash[curr]=ch
            ans=max(ans,curr_ans)
        return ans
obj=Solution()
res=obj.findMaxLength([0,1,0,2])
print(res)