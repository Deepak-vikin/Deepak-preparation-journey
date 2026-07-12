"""
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.



Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
"""

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atleast(k):
            left=0
            f={}
            count=0
            for right in range(len(nums)):
                if nums[right] in f:
                    f[nums[right]]+=1
                else:
                    f[nums[right]]=1
                while len(f)>=k:
                    if nums[left] in f:
                        if f[nums[left]]>1:
                            f[nums[left]]-=1
                        else:
                            del f[nums[left]]
                    left+=1
                count+=len(nums)-(right-left+1)
            return count
        ans=atleast(k)-atleast(k+1)
        return ans
obj=Solution()
res=obj.subarraysWithKDistinct([1,2,3,1,2],2)
print(res)