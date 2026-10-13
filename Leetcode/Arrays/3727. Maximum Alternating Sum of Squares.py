"""
You are given an integer array nums. You may rearrange the elements in any order.

The alternating score of an array arr is defined as:

score = arr[0]2 - arr[1]2 + arr[2]2 - arr[3]2 + ...
Return an integer denoting the maximum possible alternating score of nums after rearranging its elements.



Example 1:

Input: nums = [1,2,3]

Output: 12

Explanation:

A possible rearrangement for nums is [2,1,3], which gives the maximum alternating score among all possible rearrangements.

The alternating score is calculated as:

score = 22 - 12 + 32 = 4 - 1 + 9 = 12
"""
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums=[abs(i) for i in nums]
        arr=nums.sort(reverse=True)
        ans=0
        n=len(nums)
        limit=math.ceil(n/2)
        for i in range(limit):
            ans+=(nums[i]*nums[i])
        for i in range(limit,n):
            ans-=(nums[i]*nums[i])
        return ans
obj=Solution()
res=obj.maxAlternatingSum([2,3,1,1,4])
print(res)