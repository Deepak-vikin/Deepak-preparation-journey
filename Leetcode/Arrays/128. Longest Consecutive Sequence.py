"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if nums==[]:
            return 0
        freq=[0]*(max(nums)+1)
        ans=0
        count=0
        for i in nums:
            freq[i]=1
        for i in range(len(freq)):
            if freq[i]==1:
                count+=1
                ans=max(ans,count)
            else:
                count=0
        return ans
obj=Solution()
res=obj.longestConsecutive([1,2,3,4,5])
print(res)