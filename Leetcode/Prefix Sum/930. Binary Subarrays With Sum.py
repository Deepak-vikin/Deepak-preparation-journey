"""
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.



Example 1:

Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
"""
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        freq={0:1}
        pref=0
        count=0
        for i in range(len(nums)):
            pref+=nums[i]
            if pref-goal in freq:
                count+=freq[pref-goal]
            if pref in freq:
                freq[pref]+=1
            else:
                freq[pref]=1
        return count
obj=Solution()
res=obj.numSubarraysWithSum([0,1,0,1,0,1],2)
print(res)