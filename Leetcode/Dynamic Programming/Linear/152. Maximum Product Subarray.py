"""
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Note that the product of an array with a single element is the value of that element.
Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mini=nums[0]
        maxi=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            curr=nums[i]
            if curr<0:
                mini,maxi=maxi,mini
            mini=min(curr,mini*curr)
            maxi=max(curr,maxi*curr)
            ans=max(ans,maxi)
        return ans
obj=Solution()
res=obj.maxProduct([-2,0,-1])
print(res)