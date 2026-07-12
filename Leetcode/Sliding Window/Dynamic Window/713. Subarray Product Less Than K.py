"""
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.



Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left=0
        p=1
        count=0
        for right in range(len(nums)):
            p=p*nums[right]
            while p>=k:
                p=p//nums[left]
                left+=1
            if p<k:
                count+=right-left+1
        return count
obj=Solution()
res=obj.numSubarrayProductLessThanK([10,5,2,6],100)
print(res)